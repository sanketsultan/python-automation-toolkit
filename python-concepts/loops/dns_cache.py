import socket

with open("hosts.txt", "r") as file:
    hosts = file.read().splitlines()

dns_cache = {}
for host in hosts:
    try:
        ip = socket.gethostbyname(host)
        dns_cache[host] = ip
    except socket.gaierror:
        dns_cache[host] = "unresolved"

for host, ip in dns_cache.items():
    print(f"{host} -> {ip}")