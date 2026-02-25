import socket
import time

port = [80, 443, 8080, 22, 21, 25, 110, 143, 3306, 5432]

for p in port:
    s = socket.socket()
    s.settimeout(1) 
    start = time.time()
    result = s.connect_ex(("google.com", p))
    end = time.time()
    response_time = (end - start) * 1000
    if result == 0:
        print(f"Port {p} is open (Response time: {response_time:.2f} ms)")
    else:
        print(f"Port {p} is closed (Response time: {response_time:.2f} ms)")
    s.close()