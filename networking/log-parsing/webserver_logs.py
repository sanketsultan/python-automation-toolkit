with open('webserver.log', 'r') as log_file:
    lines = log_file.readlines()

ip_counts = {}
status_counts = {}
for line in lines:
        parts = line.split()
        ip = parts[0]
        status = parts[8]

        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1
        
        if status in status_counts:
            status_counts[status] += 1
        else:            status_counts[status] = 1
print("\nIP Address Counts:")
for ip, count in ip_counts.items():
    print(f"{ip} -> {count} requests")
    
print("\nStatus Code Counts:")
for status, count in status_counts.items():
    print(f"{status} -> {count} occurrences")