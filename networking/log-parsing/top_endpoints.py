import socket
with open("webserver.log", "r") as file:
    hosts = file.read().splitlines()
    count = {}
for line in hosts:
    parts = line.split()
    endpoint = parts[6]
    if endpoint in count:
        count[endpoint] += 1
    else:
        count[endpoint] = 1
sorted_endpoints = sorted(count.items(), key=lambda x: x[1], reverse=True)
print("\nTop 3 Endpoints:")
for endpoint, cnt in sorted_endpoints[:3]:
    print(f"{endpoint} -> {cnt} requests")
