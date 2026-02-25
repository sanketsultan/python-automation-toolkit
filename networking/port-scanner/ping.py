import os
import ipaddress
def ping(host):
    response = os.system("ping -c 1 -W 1 " + host + " > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

network = "8.8.8.0/28"
ipaddresss = ipaddress.ip_network(network)
for ip in ipaddresss.hosts():
    if ping(str(ip)):
        print(f"{ip} is alive")
    else:
        print(f"{ip} is unreachable")
