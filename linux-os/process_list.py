import os
print("The list of running processes is:", os.popen("ps aux").read())