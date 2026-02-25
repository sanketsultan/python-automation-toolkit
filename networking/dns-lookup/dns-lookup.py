import socket

def dns_lookup(host):
    print(f"\n=== DNS Lookup for {host} ===")
    
    try:
        # forward lookup
        ip = socket.gethostbyname(host)
        print(f"  Forward: {host} -> {ip}")
        
        # reverse lookup
        try:
            hostname = socket.gethostbyaddr(ip)
            print(f"  Reverse: {ip} -> {hostname[0]}")
        except socket.herror:
            print(f"  Reverse: {ip} -> reverse lookup blocked")
            
    except socket.gaierror:
        print(f"  Error: could not resolve {host}")

domains = ["google.com", "github.com", "booking.com", "cloudflare.com"]

for domain in domains:
    dns_lookup(domain)