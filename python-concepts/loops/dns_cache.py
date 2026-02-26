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
    
host_to_find = "google.com"
if host_to_find in dns_cache:
    print(f"\nLookup: {host_to_find} -> {dns_cache[host_to_find]}")
    
# find all unresolved hosts
print("\nUnresolved hosts:")
for host, ip in dns_cache.items():
    if ip == "unresolved":
        print(f"  {host}")

# find all resolved hosts
print("\nResolved hosts:")
for host, ip in dns_cache.items():
    if ip != "unresolved":
        print(f"  {host} -> {ip}")