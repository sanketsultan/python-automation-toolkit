import os
def ping(host):
    response = os.system("ping -c 1 -W 1 " + host)
    if response == 0:
        return True
    else:
        return False

ping("google.com")