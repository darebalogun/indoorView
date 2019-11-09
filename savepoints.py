#!/usr/bin/env python

import os
import rospy
import StartRVIZ
import time
from geometry_msgs.msg import Pose, Point, Quaternion, PointStamped
from visualization_msgs.msg import Marker, MarkerArray
from go_to_specific_point_on_map import GoToPose
from threading import Thread


class SavePoints:

    def __init__(self):
        self.navigator = GoToPose()
        self.positions = []
        self.quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : 1.000}


    def callback(self, data):
        rospy.loginfo("Point : " + str(data.point.x) + ' ' + str(data.point.y))
        position = {'x': data.point.x, 'y' : data.point.y}
        self.positions.append(position)
        

    def listener(self):

        rospy.loginfo("Please click points of interest on map in order! Press Enter when done!")

        check_done = Thread(target = self.check_for_done, args=())
        check_done.daemon = True

        check_done.start()

        rospy.Subscriber("/clicked_point", PointStamped, self.callback)

        rospy.spin()


    def check_for_done(self):
        usr_input = raw_input()
        rospy.loginfo("Saving Map...")
        os.system("gnome-terminal -x rosrun map_server map_saver -f /home/darebalogun/Desktop/maps/map")
        time.sleep(3)
        os.system("gnome-terminal -x roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/darebalogun/Desktop/maps/map.yaml")
        self.add_marker_array()
        rospy.loginfo("Estimate Initial Pose! Press Enter When Done")
        usr_input = raw_input()
        self.perform_navigation()

    
    def perform_navigation(self):
        success = self.navigator.goto(self.positions[0], self.quaternion)
        if success:
            rospy.loginfo("Hooray, reached the desired pose")
        else:
            rospy.loginfo("The base failed to reach the desired pose")


    def add_marker_array(self):
        publisher = rospy.Publisher("visualization_marker_array", MarkerArray)
        markerArray = MarkerArray()
        
        marker = Marker()
        marker.header.frame_id = "map"
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = self.positions[0]['x']
        marker.pose.position.y = self.positions[0]['y']
        marker.id = 0
        markerArray.markers.append(marker)

        publisher.publish(markerArray)

if __name__ == '__main__':
    
    rospy.init_node('listener', anonymous=True)
    savepoints = SavePoints()
    savepoints.listener()