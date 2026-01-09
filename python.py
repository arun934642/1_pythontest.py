#How do you check the installed Python version using shell & Python:
# Using Shell:
# Open your terminal or command prompt and type
# python --version
import sys
print("Python version", sys.version)
print(f"Version info: {sys.version_info}")

# 2.In Shell, print the current username (whoami) , In Python, use os.getlogin().
import os
current_user = os.getlogin()
print("current user:", current_user)

#3.Use Shell to display the current working directory (pwd), Write a Python script using os.getcwd().
import os
current_directory = os.getcwd()
print("current working directory:", current_directory)

#4.In Shell, to get cpu count we use nproc, Write a script using psutil.
import psutil
cpu_count = psutil.cpu_count(logical=True)
print("CPU Count:", cpu_count)

#5.In Shell, print system uptime (uptime), In Python, use psutil.boot_time().
import time
boot_time_timestamp = psutil.boot_time()
bt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot_time_timestamp))
print("System Boot Time:", bt)

#6.List all environment variables in Shell (printenv), Do the same in Python using os.environ.
import os
env_vars = os.environ
print("Environment Variables:", env_vars)

#7.Write a Shell script to check memory usage (free -h), Write the Python equivalent using psutil.virtual_memory().
import psutil
memory = psutil.virtual_memory()
print("Memory Usage:", memory)

#8.In Shell, display the date and time (date), In Python, use datetime.now().
import datetime
now = datetime.datetime.now()
print("Current Date and Time:", now)

#9.Run a Shell command (ls -l) from Python using the subprocess module.
import subprocess

result = subprocess.run(
    ["ls", "-l"],
    capture_output=True,
    text=True
)
print(result.stdout)











