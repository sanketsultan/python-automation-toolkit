import socket
with open("hosts.txt", "r") as file:
    hosts = file.read().splitlines()

for host in hosts:
    attempts = 0        # ← reset for each host
    max_attempts = 3
    
    while attempts < max_attempts:
        try:
            ip = socket.gethostbyname(host)
            print(f"{host} -> {ip}")
            break
        except socket.gaierror:
            attempts += 1
            print(f"Attempt {attempts} failed for {host}")
    
    if attempts == max_attempts:
        print(f"{host} unreachable after {max_attempts} attempts")