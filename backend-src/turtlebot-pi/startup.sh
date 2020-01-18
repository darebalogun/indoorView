#!/bin/bash
source /opt/ros/kinetic/setup.bash
source ~/catkin_ws/devel/setup.bash
python /home/pi/Desktop/NetworkConfigRPi.py
source ~/.bashrc
python /home/pi/Desktop/StartRoslaunch.py
