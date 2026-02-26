import socket

with open("hosts.txt", "r") as file:
    hosts = file.read().splitlines()
    
def ping_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

for host in hosts:
    if ping_host(host):
        print(f"{host} is reachable")
    else:
        print(f"{host} is unreachable")