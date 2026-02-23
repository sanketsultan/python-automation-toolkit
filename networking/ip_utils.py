import ipaddress

net = ipaddress.ip_network('192.168.1.0/24')
print(net.num_addresses)       # 256
print(net.network_address)     # 192.168.1.0
print(net.broadcast_address)   # 192.168.1.255

# Check if IP is in subnet
ip = ipaddress.ip_address('192.168.1.50')
print(ip in net)  # True

# Subnetting
subnets = list(net.subnets(prefixlen_diff=1))  # Split into /25s