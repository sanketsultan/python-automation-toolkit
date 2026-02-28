#Find all zombie/defunct processes and print their PID and name.
import os
import time
import psutil
while True:
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        if proc.info['status'] == psutil.STATUS_ZOMBIE:
            print(f"Zombie Process Found - PID: {proc.info['pid']}, Name: {proc.info['name']}")
    time.sleep(5)