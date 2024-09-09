import subprocess
import time
import json
import pandas as pd

# Azure configuration
resource_group = 'vAPVwestus'
public_ip = 'vmtestpublicip0'

#------------------------------------------------------------------------------#

def run_az_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"Error executing command: {result.stderr}")
            return None

#------------------------------------------------------------------------------#

# GET THE STATUS OF VM
def get_vm_status(resource_group, vm_name):
    command = [
        'az', 'vm', 'get-instance-view',
        '--resource-group', resource_group,
        '--name', vm_name,
        '--query', "instanceView.statuses[?starts_with(code, 'PowerState/')].displayStatus",
        '--output', 'tsv'
    ]

    output = run_az_command(command)
    if output:
        statuses = output.strip().split('\n')
        for status in statuses:
            power_state = status.split('/')[-1] if '/' in status else status
            power_state = power_state.replace('VM ', '')

        return power_state
    return []

#------------------------------------------------------------------------------#

# GET ALL VM IN A RESOURCE GROUP
def get_all_VM(resource_group):
    vm_command = [
        'az', 'vm', 'list', '--resource-group',
        resource_group, '--query', "[].name", '--output', 'tsv'
    ]

    virtual_machines = run_az_command(vm_command)
    if virtual_machines:
        vm_list = virtual_machines.strip().split('\n')
        return vm_list
    return []

#------------------------------------------------------------------------------#

# GET THE NIC NAME OF VM
def get_nicname(resource_group):
    nic_command = [
        'az', 'network', 'nic', 'list', '--resource-group',
        resource_group, '--query', "[].{Name:name, IPConfigs:ipConfigurations[*].name}",
        '--output', 'table'
    ]

    nic_name = run_az_command(nic_command)
    if nic_name:
        nic_list = nic_name.split('\n')
        nic_list = nic_list[2:]  # Skip the header rows
        if nic_list:
            return [line.split()[0] for line in nic_list if line]
    return []

#------------------------------------------------------------------------------#

# GET IP CONFIG NAME
def get_ipconfig(resource_group, nic_name):
    ipconfig_command = [
        'az', 'network', 'nic', 'show', '--resource-group',
        resource_group, '--name', nic_name, '--query',
        "ipConfigurations[*].{Name:name}", '--output', 'table'
    ]

    ipname = run_az_command(ipconfig_command)
    if ipname:
        ipconfig_list = ipname.split('\n')
        ipconfig_list = ipconfig_list[2:]  # Skip the header rows
        if ipconfig_list:
            return ipconfig_list[0].split()[0]  # Return the first IP config name
    return ""

#------------------------------------------------------------------------------#

# REASSOCIATE PUBLIC IP
def reassociateIp_vm(resource_group, ipconfig_name, nic_name, public_ip):
    reassociate_command = [
        'az', 'network', 'nic', 'ip-config', 'update', '--name',
        ipconfig_name, '--resource-group', resource_group, '--nic-name', nic_name,
        '--public-ip-address', public_ip
    ]

    run_az_command(reassociate_command)

#------------------------------------------------------------------------------#

# GET PUBLIC IP
def get_public_ip(resource_group, vm_name):
    ip_address_command = [
        'az', 'vm', 'show', '-d', '--resource-group', resource_group,
        '--name', vm_name, '--query', 'publicIps', '-o', 'tsv'
    ]

    ip_address = run_az_command(ip_address_command)
    if ip_address:
        return ip_address.strip()
    return ""

#------------------------------------------------------------------------------#

# START A VM
def startup_vm(resource_group, vm_name):
    startup_command = [
        'az', 'vm', 'start', '--resource-group', resource_group,
        '--name', vm_name
    ]

    run_az_command(startup_command)

#------------------------------------------------------------------------------#

def main():
    vm_names = get_all_VM(resource_group)
    nic_names = get_nicname(resource_group)

    while True:
        print("Fetching VM status...")

        statuses = []
        ipaddress = []
        ipconfig_names = []

        for num in range(len(vm_names)):
            statuses.append(get_vm_status(resource_group, vm_names[num]))
            ipaddress.append(get_public_ip(resource_group, vm_names[num]))
            ipconfig_names.append(get_ipconfig(resource_group, nic_names[num]))

        info_dict = {
            "VM Name": vm_names,
            "Power State": statuses,
            "IP Address": ipaddress
        }

        info_chart = pd.DataFrame(info_dict)
        print(info_chart)
        print()

        for numvm in range(len(vm_names)):
            power_state = statuses[numvm]
            if power_state == "running" and ipaddress[numvm] != "":
                result = subprocess.run(['python3', 'accessvm.py'], capture_output=True, text=True)
                server_status = result.stdout.strip()
                print(server_status)

                if server_status != "active":
                    print("Server not active")

            if power_state == "deallocated" or power_state == "stopped":
                if numvm > 0 and statuses[numvm - 1] != "deallocated":
                    if ipaddress[numvm] != "":
                        print(f"Disassociating public IP from {vm_names[numvm]}")
                        reassociateIp_vm(resource_group, ipconfig_names[numvm], nic_names[numvm], '')
                        print(f"Successfully disassociated public IP. Associating public IP.")
                        reassociateIp_vm(resource_group, ipconfig_names[numvm], nic_names[numvm], public_ip)
                        print("Successfully associated public IP.\n")

                # Code for if you want to start up the deallocated VM again
                # else:
                #     print(f"Starting up {vm_names[numvm]}")
                #     startup_vm(resource_group, vm_names[numvm])

        # Wait before the next update
        time.sleep(30)

if __name__ == "__main__":
    main()
