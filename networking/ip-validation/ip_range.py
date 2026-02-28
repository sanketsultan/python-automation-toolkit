with open("ip_logs.log", "r") as file:
    ip_ranges = file.read().splitlines()

def is_ip_in_range(ip, ip_range):
    ip_parts = list(map(int, ip.split('.')))
    range_parts = ip_range.split('-')
    start_ip = list(map(int, range_parts[0].split('.')))
    end_ip = list(map(int, range_parts[1].split('.')))
    
    # Check if IP is in range
    for i in range(4):
        if ip_parts[i] < start_ip[i] or ip_parts[i] > end_ip[i]:
            print(f"{ip} is not in the range {ip_range}")
            return False
    
    # Generate IPs from given IP to end of range
    range_ips = []
    for i in range(ip_parts[3], end_ip[3] + 1):
        range_ips.append(f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{i}")
    
    print(f"IPs from {ip} to end of range: {', '.join(range_ips)}")
    return True
    
is_ip_in_range("10.0.1.2", "10.0.1.0-10.0.1.5")