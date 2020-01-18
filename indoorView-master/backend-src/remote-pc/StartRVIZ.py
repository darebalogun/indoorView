import os

os.system("gnome-terminal -x roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=hector")
os.system("gnome-terminal -x roslaunch teleop_twist_joy teleop.launch")

