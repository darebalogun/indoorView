import netifaces as ni
import ipaddress
import os

# Get pc ip
pc_IP = ni.ifaddresses('wlp2s0')[ni.AF_INET][0]['addr']
print("PC IP address: " + pc_IP)

bashrc_path = os.path.expanduser('~/.bashrc')

with open(bashrc_path, 'r') as file:
    lines = file.readlines()

lines[126] = "export ROS_MASTER_URI=http://" + pc_IP + ":11311\n"
lines[127] = "export ROS_HOSTNAME=" + pc_IP + "\n"

with open(bashrc_path, 'w') as file:
    file.writelines(lines)

os.system(". " + bashrc_path)

os.system("gnome-terminal --command='roscore'")
