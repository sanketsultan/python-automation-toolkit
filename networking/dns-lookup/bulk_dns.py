import ipaddress
import socket

with open("ips.txt", "r") as file:
    hosts = file.read().splitlines()
    
for ip in hosts:
    try:
        ipaddress.ip_address(ip)
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            print(f"{ip} -> {hostname}")
        except socket.herror:
            print(f"{ip} -> No hostname found")
    except ValueError:
        print(f"{ip} is not a valid IP address")