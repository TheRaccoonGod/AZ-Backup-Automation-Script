import paramiko


def run_command_on_vm(ssh_client, command):
     stdin, stdout, stderr  = ssh_client.exec_command(command)
     output = stdout.read().decode()
     error = stderr.read().decode()

     if output:
         return output
     if error:
         return error


def main():
     username = 'array'
     password = 'ArrayAdmin1111'
     hostname = '13.88.56.124'
     port = 22

     ssh_client = paramiko.SSHClient()
     ssh_client.load_system_host_keys()
     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     ssh_client.connect(hostname, port=port, username=username, password=passw$


     active_status = run_command_on_vm(ssh_client, 'systemctl is-active mysql')

     print(active_status)

     ssh_client.close()


if __name__ == "__main__":
     main()
