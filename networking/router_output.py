import re

output = """
Routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.0.0        0.0.0.0         255.0.0.0       U     0      0        0 eth0
10.0.0.1        0.0.0.0         255.255.255.255 U     0      0        0 eth0
"""

pattern = r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'
matches = re.findall(pattern, output)
for match in matches:
    destination, gateway, genmask, flags = match
    print(f"Destination: {destination}, Gateway: {gateway}, Genmask: {genmask}, Flags: {flags}")