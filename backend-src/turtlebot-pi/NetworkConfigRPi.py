import netifaces as ni
import ipaddress
import os

# Get Raspberry Pi IP address
rpi_IP = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']

# Static IP of remote PC
pc_IP = '172.17.130.62'

print("IP address of RPi: " + rpi_IP)

print("IP address of PC: " + pc_IP)

with open('/home/pi/.bashrc', 'r') as file:
    lines = file.readlines()

lines[128] = "export ROS_MASTER_URI=http://" + pc_IP + ":11311\n"
lines[129] = "export ROS_HOSTNAME=" + rpi_IP + "\n"

with open('/home/pi/.bashrc', 'w') as file:
    file.writelines(lines)

