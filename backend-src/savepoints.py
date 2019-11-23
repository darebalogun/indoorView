#!/usr/bin/env python

import os
import rospy
import StartRVIZ
import time
import splitpoints
from savetodatabase import Database
from geometry_msgs.msg import Pose, Point, Quaternion, PointStamped
from visualization_msgs.msg import Marker, MarkerArray
from go_to_specific_point_on_map import GoToPose
from threading import Thread
from PIL import Image


class MapPoints:
    '''
    Class represents set of points of interest through which the turtlebot will travel.
    The turtlebot will also take a 360 photo at each photo and save images to database
    '''

    def __init__(self, name):
        self.name = name
        # Navigator to send goals on map to turtlebot
        self.navigator = GoToPose()
        # Array of position objects. Each position is 2 long python dictionary with 'x' and 'y' keys with positions
        self.positions = []
        # TODO: Calculate quaternion based on previous point
        self.quaternion = {'r1': 0.000, 'r2': 0.000, 'r3': 0.000, 'r4': 1.000}
        # Publish points on map
        self.publisher = rospy.Publisher(
            "/visualization_marker", Marker, queue_size=5)
        self.marker_id_count = 0
        self.database = Database()
        self.database.create_table(self.name)
        self.map_size = 160
        self.map_resolution = 0.05

    def callback(self, data):
        rospy.loginfo("Point : " + str(data.point.x) + ' ' + str(data.point.y))
        while True:
            if not self.positions:
                a = (0, 0)
            else:
                a = (self.positions[-1]['x'], self.positions[-1]['y'])

            b = (data.point.x, data.point.y)

            midx, midy = splitpoints.get_split_point(a, b, 0.5)

            if not (a[0] <= midx <= b[0] or b[0] <= midx <= a[0]):
                position = {'x': data.point.x, 'y': data.point.y}
                self.positions.append(position)
                self.add_marker(position)
                break

            position = {'x': midx, 'y': midy}
            self.positions.append(position)
            self.add_marker(position)

    def listener(self):

        rospy.loginfo(
            "Please click points of interest on map in order! Press Enter when done!")
        check_done = Thread(target=self.check_for_done, args=())
        check_done.daemon = True
        check_done.start()
        rospy.Subscriber("/clicked_point", PointStamped, self.callback)
        rospy.spin()

    def check_for_done(self):
        usr_input = raw_input()

        rospy.loginfo("Saving Map...")
        os.system(
            "gnome-terminal -x rosrun map_server map_saver -f /home/darebalogun/Desktop/Turtlebot/turtlebot/frontend-webapp/maps/" + self.name)
        rospy.sleep(3)
        Image.open("../maps/" + self.name +
                   ".pgm").save("../maps/" + self.name + ".png")
        self.database.add_map(self.name, "maps/" + self.name + ".png")
        os.system("gnome-terminal -x roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/darebalogun/Desktop/Turtlebot/turtlebot/frontend-webapp/maps/" + self.name + ".yaml")
        rospy.loginfo("Estimate Initial Pose! Press Enter When Done")
        rospy.sleep(3)
        self.add_marker_array()
        usr_input = raw_input()
        self.perform_navigation()

    def perform_navigation(self):
        for position in self.positions:
            success = self.navigator.goto(position, self.quaternion)
            if success:
                rospy.loginfo("Hooray, reached the desired pose")
            else:
                rospy.loginfo("The base failed to reach the desired pose")

            rospy.sleep(1)

    def add_marker(self, position):
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = rospy.Time.now()
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.scale.x = 0.1
        marker.scale.y = 0.1
        marker.scale.z = 0.1
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = position['x']
        marker.pose.position.y = position['y']
        marker.id = self.marker_id_count
        self.marker_id_count += 1
        self.publisher.publish(marker)
        coordinates = str(position['x']) + ',' + str(position['y'])
        mappedx = position['x']/self.map_resolution + self.map_size/2
        mappedy = -1*position['y']/self.map_resolution + self.map_size/2
        self.database.add_coordinate(
            self.name, coordinates, "images/360.jpg", mappedx, mappedy)

    def add_marker_array(self):
        for position in self.positions:
            self.add_marker(position)


if __name__ == '__main__':

    rospy.init_node('listener', anonymous=True)
    mappoints = MapPoints("projectroom")
    mappoints.listener()
