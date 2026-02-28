import os
print("The current working directory is:", os.getcwd())
print("The list of files and directories in the current directory is:", os.listdir())
print("The size of the current directory is:", os.path.getsize(os.getcwd()), "bytes")
print("The absolute path of the current directory is:", os.path.abspath(os.getcwd()))