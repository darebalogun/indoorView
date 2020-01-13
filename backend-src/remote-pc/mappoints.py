#!/usr/bin/env python

import os
import rospy
import StartRVIZ
import splitpoints
import showmap
import h_udp_client
from time import time
from PIL import Image
from savetodatabase import Database
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty
from std_srvs.srv import Empty
from geometry_msgs.msg import Pose, Point, Quaternion, PointStamped
from visualization_msgs.msg import Marker, MarkerArray
from go_to_specific_point_on_map import GoToPose
from threading import Thread


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

        # Publisher for points on map
        self.publisher = rospy.Publisher(
            "/visualization_marker", Marker, queue_size=10)

        # Marker ids have to be different to show
        self.marker_id_count = 0

        self.database = Database()

        # Create table in database for our map
        self.database.create_table(self.name)

        # Default map size in pixes can be found in rviz map launch file
        self.map_size = 160

        # Default map resolution in meters/pixel;
        self.map_resolution = 0.05

        # Between points on map to take photo in meters
        self.photo_spacing = 0.5

    def get_location(self, data):
        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y

    def callback(self, data):
        """
        callback function is called whenever there a publish on the /clicked_point topic i.e whenever a published point
        is added in rviz. 

        Parameters
        ----------
        data :
            Information on which publish triggered the callback. In this case the data on the clicked point
        """

        rospy.loginfo("Point : " + str(data.point.x) + ' ' + str(data.point.y))

        # Interpolate between points of interest
        while True:
            # TODO get starting point of robot here instead of (0,0)
            if not self.positions:
                a = (0, 0)
                '''
                a = (self.x,
                     self.y)
                '''
                print(a)
            else:
                a = (self.positions[-1]['x'], self.positions[-1]['y'])

            b = (data.point.x, data.point.y)

            midx, midy = splitpoints.get_split_point(a, b, self.photo_spacing)

            if not (a[0] <= midx <= b[0] or b[0] <= midx <= a[0]):
                position = {'x': data.point.x, 'y': data.point.y}
                self.positions.append(position)
                self.add_marker(position)
                break

            position = {'x': midx, 'y': midy}
            self.positions.append(position)
            self.add_marker(position)

    def listener(self):
        """
        Start listening for published points on the map
        """
        rospy.loginfo(
            "Please click points of interest on map in order! Press Enter when done!")

        # Create separate thread to listen for done
        check_done = Thread(target=self.check_for_done, args=())
        check_done.daemon = True
        check_done.start()

        # Subscribe to the /clicked_point topic
        rospy.Subscriber("/clicked_point", PointStamped, self.callback)
        rospy.Subscriber("/odom", Odometry, self.get_location)

        # TODO reset odom
        rospy.wait_for_service("/gazebo/reset_world")
        reset_world = rospy.ServiceProxy("/gazebo/reset_world", Empty)
        for x in range(100):
            reset_world()

        rospy.loginfo("Shutting down")
        rospy.spin()

    def check_for_done(self):
        """
        Wait for the user to press enter to indicate done then process map and save info in database 
        """
        raw_input()

        rospy.loginfo("Saving Map...")
        os.system(
            "gnome-terminal -x rosrun map_server map_saver -f /home/darebalogun/Desktop/Turtlebot/turtlebot/frontend-webapp/maps/" + self.name)
        rospy.sleep(3)

        # Convert to png and save as png and save to db
        Image.open("../../frontend-webapp/maps/" + self.name +
                   ".pgm").save("../../frontend-webapp/maps/" + self.name + ".png")
        self.database.add_map(self.name, "maps/" + self.name + ".png")

        # Launch self navigation node
        os.system("gnome-terminal -x roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/darebalogun/Desktop/Turtlebot/turtlebot/frontend-webapp/maps/" + self.name + ".yaml")
        rospy.loginfo("Estimate Initial Pose! Press Enter When Done")
        rospy.sleep(3)

        # Publish markers on navigation node map
        self.add_marker_array()

        # Wait for user to press enter when done then navigate
        raw_input()
        self.perform_navigation()

    def perform_navigation(self):
        """
        Autonomous navigation to every position saved in self.positions
        """
        for position in self.positions:
            # TODO update quaternions
            success = self.navigator.goto(position, self.quaternion)
            if success:
                rospy.loginfo("Hooray, reached the desired pose")
            else:
                rospy.loginfo("The base failed to reach the desired pose")

            # TODO Add image capture, processing and storage code here
            h_udp_client.hUDPClient("capture", self.name)

        # TODO Add code to rename and transfer data
        h_udp_client.hUDPClient("save_all_images", self.name)

    def add_marker(self, position):
        """
        Adds marker to the plot, and to the database

        Parameters
        ----------
        position : dict
            'x' : x coordinate
            'y' : y coordinate
        """
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

        # ROS coordinates have origin in centre of map, so we need to map to a coordinate system with origin in top left
        coordx = position['x']
        coordy = position['y']
        mappedx = position['x']/self.map_resolution + self.map_size/2
        mappedy = -1*position['y']/self.map_resolution + self.map_size/2

        # Add both sets of coordinates to database with image path
        # TODO get image path from camera capture module
        self.database.add_coordinate(
            self.name, coordx, coordy, "images/360.jpg", mappedx, mappedy)

    def add_marker_array(self):
        """
        Add all markers
        """
        for position in self.positions:
            self.add_marker(position)


if __name__ == '__main__':
    mapname = raw_input("Please enter a name for the map: ")
    rospy.init_node('listener', anonymous=True)
    mappoints = MapPoints(mapname)
    mappoints.listener()
