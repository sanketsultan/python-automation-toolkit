import socket
import ipaddress


def get_unique_ips_from_log(file_path):
    unique_ips = []
    seen = set()

    with open(file_path, "r") as log_file:
        for line in log_file:
            parts = line.split()
            if not parts:
                continue

            ip = parts[0]
            if ip not in seen:
                seen.add(ip)
                unique_ips.append(ip)

    return unique_ips


def scan_host_ports(ip, ports):
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"Port {port} is open on {ip}")
        else:
            print(f"Port {port} is closed on {ip}")


unique_ips = get_unique_ips_from_log("webserver.log")

for ip in unique_ips:
    try:
        ipaddress.ip_address(ip)
        scan_host_ports(ip, [80, 443])
    except ValueError:
        print(f"{ip} is not a valid IP address")