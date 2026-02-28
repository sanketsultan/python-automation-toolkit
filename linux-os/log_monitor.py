import os
print("The last 10 lines of the log file are:", os.popen("tail -n 10 /var/log/system.log").read())