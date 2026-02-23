#Given a list of IPs, find the smallest supernet that contains all of them.

import ipaddress
def find_supernet(ip_list):
    # Convert the list of IPs to a list of ipaddress.IPv4Address objects
    ip_objects = [ipaddress.IPv4Address(ip) for ip in ip_list]
    
    # Find the minimum and maximum IP addresses
    min_ip = min(ip_objects)
    max_ip = max(ip_objects)
    
    # Calculate the supernet that contains both min_ip and max_ip
    supernet = ipaddress.summarize_address_range(min_ip, max_ip)
    
    return list(supernet)
# Example usage:
if __name__ == "__main__":
    ip_list = ['192.168.1.1', '192.168.1.2', '192.168.1.3']
    supernet = find_supernet(ip_list)
    for net in supernet:
        print(net)