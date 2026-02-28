import os
import time
folder_path = 'python-automation-toolkit/linux-os/auto_cleanup_folder'
while True:
    current_time = time.time()
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_age = current_time - os.path.getmtime(file_path)
            if file_age > 7 * 24 * 60 * 60:  # Older than 7 days
                os.remove(file_path)
                print(f"Deleted: {file_path}")
    time.sleep(24 * 60 * 60)  # Check once a day