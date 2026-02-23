#Given a list of IP prefixes, find which ones overlap with each other.
import ipaddress
def find_overlaps(prefix_list):
    # Convert the list of prefixes to a list of ipaddress.IPv4Network objects
    networks = [ipaddress.IPv4Network(prefix) for prefix in prefix_list]
    
    overlaps = []
    for i in range(len(networks)):
        for j in range(i + 1, len(networks)):
            if networks[i].overlaps(networks[j]):
                overlaps.append((str(networks[i]), str(networks[j])))
    
    return overlaps
# Example usage:
if __name__ == "__main__":
    prefix_list = ['192.168.1.0/24', '192.168.1.128/25', '10.0.0.0/8']
    overlaps = find_overlaps(prefix_list)
    for overlap in overlaps:
        print(f"Overlap found between {overlap[0]} and {overlap[1]}")