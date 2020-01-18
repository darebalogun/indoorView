import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

map_size = int(config['MAP']['MapSize']) / \
    float(config['MAP']['MapResolution'])

os.system("gnome-terminal -x roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=hector map_size:=" +
          str(map_size) + " map_resolution:=" + config['MAP']['MapResolution'])
os.system("gnome-terminal -x roslaunch teleop_twist_joy teleop.launch")


def get_map_size():
    return map_size


def get_map_resolution():
    return float(config['MAP']['MapResolution'])


def get_photo_spacing():
    return float(config['MAP']['PhotoSpacing'])
