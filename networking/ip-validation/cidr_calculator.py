import ipaddress

def cidr_calculator(cidr):
    network = ipaddress.ip_network(cidr)
    hosts = list(network.hosts())
    
    print(f"Network:           {network}")
    print(f"Network Address:   {network.network_address}")
    print(f"Broadcast Address: {network.broadcast_address}")
    print(f"Total IPs:         {network.num_addresses}")
    print(f"Usable Hosts:      {len(hosts)}")
    print(f"First Usable IP:   {hosts[0]}")
    print(f"Last Usable IP:    {hosts[-1]}")

cidr_calculator("192.168.1.0/24")
cidr_calculator("10.0.0.0/16")