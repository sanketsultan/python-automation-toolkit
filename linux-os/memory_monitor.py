import os
import time
import psutil
while True:
    mem = psutil.virtual_memory()
    total_memory = mem.total / (1024 * 1024)  # Convert to MB
    used_memory = mem.used / (1024 * 1024)    # Convert to MB
    free_memory = mem.free / (1024 * 1024)    # Convert to MB
    memory_usage_percent = mem.percent

    print(f"Total Memory: {total_memory:.2f} MB")
    print(f"Used Memory: {used_memory:.2f} MB")
    print(f"Free Memory: {free_memory:.2f} MB")
    print(f"Memory Usage: {memory_usage_percent}%")

    if memory_usage_percent > 70:
        print("ALERT: Memory usage is above 70%!")
    
    time.sleep(2)