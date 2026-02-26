import socket
with open("hosts.txt", "r") as file:
    hosts = file.read().splitlines()

for host in hosts:
    try:
        dns_lookup = socket.gethostbyname(host)
        print(f"{host} -> {dns_lookup}")
    except socket.gaierror:
        print(f"  Error: could not resolve {host}")