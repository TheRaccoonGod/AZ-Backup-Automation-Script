''' 

Task: Make a script that runs 100 requests, 100 connections, run for 10 minutes per docker for ip 172.16.2.10 to ip 172.16.2.22

docker run --rm --network net1 --ip 172.16.2.10 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.11 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.12 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.13 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.14 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.15 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.16 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.17 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.18 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.19 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.20 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.21 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
docker run --rm --network net1 --ip 172.16.2.22 ab-docker ab -n 100 -c 100 -k -t 600 \
-H "Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true" \
https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &
wait

'''







import subprocess
import ipaddress

def run_command(command):

     result = subprocess.run(command, shell = True, check = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)

     if result.stdout:
          print("The code successfully ran")

     if result.stderr:
          print("There was an error")


def main():
     first_ip_num = 10
     last_ip_num = 22

     network = ipaddress.IPv4Network(f'192.0.2.{first_ip_num}/24', strict=False)
     ip_list = [str(ip) for ip in network.hosts() if ipaddress.IPv4Address(f'192.0.2.{first_ip_num}') <= ip <= ipaddress.IPv4Address(f'192.0.2.{last_ip_num}')]

     for ip_num in ip_list:
          run_command(f"docker run --rm --network net1 --ip {ip_num} ab-docker ab -n 100 -c 100 -k -t 600 "
                      f"-H 'Cookie: ANsession3714112571002576=vpnportal01+91bf6bea_a16a8b889aa55556fb79bade34bb3618; username=user1; "
                      f"role_xid=3psJpIvo1Jggt6t673hp42MQo1PwSsqQ%7cQKKa02mQMGyi%3b_Dwuv6_; "
                      f"role_names=LocalDB; AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d91bf6bea%26eoc; vpn_auto=true' "
                      f"https://20.20.10.10:4432/prx/000/https/192.168.2.2/lab/ecw.html &")


if __name__ == "__main__":
    main()
