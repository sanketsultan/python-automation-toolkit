with open('ip_logs.log', 'r') as file:
    lines = file.readlines()
ips = [line.split()[0] for line in lines]
def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        print(f"{ip} is invalid: Incorrect number of parts")
        return False
    for part in parts:
        if not part.isdigit():
            print(f"{ip} is invalid: Non-numeric part detected")
            return False
        num = int(part)
        if num < 0 or num > 255:
            print(f"{ip} is invalid: Part {num} out of range (0-255)")
            return False
    return True
for ip in ips:
    if is_valid_ip(ip):
        print(f"{ip} is valid")