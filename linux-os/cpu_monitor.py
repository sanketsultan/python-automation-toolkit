import os
import time
import psutil
while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU usage: {cpu_usage}%")
    if cpu_usage > 80:
        print("ALERT: CPU usage is above 80%!")
    time.sleep(2)