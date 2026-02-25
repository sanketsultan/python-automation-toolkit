with open('webserver.log', 'r') as log_file:
    lines = log_file.readlines()

ip_counts = {}
suspicious_counts = {}
for line in lines:
    parts = line.split()
    ip = parts[0]
    status = parts[8]

    ip_counts == ip_counts.get(ip, 0) + 1
    
    if status == '401':
        suspicious_counts[ip] = suspicious_counts.get(ip, 0) + 1

print("\nSuspicious IP Addresses (401 Unauthorized):")
for ip, count in suspicious_counts.items():
    if count > 2:
        print(f"{ip} -> {count} unauthorized attempts")
