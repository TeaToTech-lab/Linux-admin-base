import os
import shutil
# Specify the directory name
directory_name = "/root/config_bkp/"

# Create the directory
try:
    os.mkdir(directory_name)
    print(f"Config Backup Directory '{directory_name}' created successfully.")
except FileExistsError:
    print(f"Config Backup Directory '{directory_name}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{directory_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")

#list Ip routes

cmd = 'ip route list'

output_file = "/root/config_bkp/ip-routes.txt"

# using os.system to run the command and redirect the output to a file
execute = os.system(f"{cmd} > {output_file}")
if execute == 0:
    print("Successfully executed")
else:
    print("Failed")
os.system(cmd)

cmd1 = 'cat /etc/os-release'

output_file = "/root/config_bkp/os-release.txt"

# using os.system to run the command and redirect the output to a file
execute = os.system(f"{cmd1} > {output_file}")
if execute == 0:
    print("Successfully executed")
else:
    print("Failed")
os.system(cmd1)

cmd2 = 'cat /etc/sysctl.conf'

output_file = "/root/config_bkp/sysctl.conf_bkp.txt"

# using os.system to run the command and redirect the output to a file
execute = os.system(f"{cmd2} > {output_file}")
if execute == 0:
    print("Successfully executed")
else:
    print("Failed")
os.system(cmd2)

# cmd4='rpm -qa|sort '
cmd4='dpkg -l|sort'
output_file = "/root/config_bkp/package_list_bkp.txt"

# using os.system to run the command and redirect the output to a file
execute = os.system(f"{cmd4} > {output_file}")
if execute == 0:
    print("Successfully executed")
else:
    print("Failed")
os.system(cmd4)


