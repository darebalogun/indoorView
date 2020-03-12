#!/usr/bin/env python

import os
import rospy
import StartRVIZ
import splitpoints
import showmap
import message_client
import subprocess
import anglebtwnpoints
import pyquaternion
import localization
import time
import math
from PIL import Image
from savetodatabase import Database
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty
from geometry_msgs.msg import Pose, Point, Quaternion, PointStamped, PoseWithCovarianceStamped
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

        # Array of quaternions
        self.orientations = []

        # TODO: Calculate quaternion based on previous point
        #                   x               y           z           w
        self.quaternion = {'x': 0.000, 'y': 0.000, 'z': 0.000, 'w': 1.000}

        # Publisher for points on map
        self.publisher = rospy.Publisher(
            "/visualization_marker", Marker, queue_size=10)

        # Marker ids have to be different to show
        self.marker_id_count = 0

        self.database = Database()

        # Create table in database for our map
        self.database.create_table(self.name)

        # Default map size in pixes can be found in rviz map launch file
        self.map_size = StartRVIZ.get_map_size()

        # Default map resolution in meters/pixel;
        self.map_resolution = StartRVIZ.get_map_resolution()

        # Between points on map to take photo in meters
        self.photo_spacing = StartRVIZ.get_photo_spacing()

        # Save locatio for map
        self.map_path = "/home/darebalogun/Desktop/Turtlebot/turtlebot/frontend-webapp/maps/" + self.name

        self.template_path = "/home/darebalogun/Desktop/Turtlebot/turtlebot/frontend-webapp/templates/" + \
            self.name + "_template"

    def get_location(self, data):
        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y

        self.orientation = data.pose.pose.orientation

    def callback(self, data):
        """
        callback function is called whenever there a publish on the /clicked_point topic i.e whenever a published point
        is added in rviz.

        Parameters
        ----------
        data :
            Information on which publish triggered the callback. In this case the data on the clicked point
        """

        #rospy.loginfo("Point : " + str(data.point.x) + ' ' + str(data.point.y))

        '''
        # Interpolate between points of interest
        while True:
            # TODO get starting point of robot here instead of (0,0)
            if not self.positions:
                a = (self.x,
                     self.y)

                pose = {'x': self.orientation.x, 'y': self.orientation.y,
                        'z': self.orientation.z, 'w': self.orientation.w}
            else:
                a = (self.positions[-1]['x'], self.positions[-1]['y'])
                pose = self.orientations[-1]

            b = (data.point.x, data.point.y)

            midx, midy = splitpoints.get_split_point(a, b, self.photo_spacing)

            if not (a[0] <= midx <= b[0] or b[0] <= midx <= a[0]):'''

        if not self.positions:
            a = (0, 0)
        else:
            a = (self.positions[-1]['x'], self.positions[-1]['y'])
        position = {'x': data.point.x, 'y': data.point.y}
        self.positions.append(position)
        self.add_marker(position)
        angle = -1 * \
            anglebtwnpoints.getangle(a, (position['x'], position['y']))
        rotation = pyquaternion.Quaternion(
            axis=[0.0, 0.0, 1.0], radians=angle)
        new_pose = {'x': rotation.elements[1], 'y': rotation.elements[2],
                    'z': rotation.elements[3], 'w': rotation.elements[0]}
        # print(angle)
        self.orientations.append(new_pose)
        '''
            break

        position = {'x': midx, 'y': midy}
        self.positions.append(position)
        self.add_marker(position)
        angle = -1 * \
            anglebtwnpoints.getangle(a, (position['x'], position['y']))
        rotation = pyquaternion.Quaternion(
            axis=[0.0, 0.0, 1.0], radians=angle)
        new_pose = {'x': rotation.elements[1], 'y': rotation.elements[2],
                    'z': rotation.elements[3], 'w': rotation.elements[0]}
        print(angle)
        self.orientations.append(new_pose)
        '''

    def listener(self):
        """
        Start listening for published points on the map
        """

        # Create separate thread to listen for done
        # check_done = Thread(target=self.check_for_done, args=())
        # check_done.daemon = True
        # check_done.start()

        # Subscribe to the /clicked_point topic
        rospy.Subscriber("/clicked_point", PointStamped, self.callback)
        rospy.Subscriber("/odom", Odometry, self.get_location)
        rospy.spin()

    def check_for_done(self):
        """
        Wait for the user to press enter to indicate done then process map and save info in database
        """

        rospy.loginfo("Saving Map...")
        os.system(
            "gnome-terminal -x rosrun map_server map_saver -f " + self.map_path)
        rospy.sleep(3)

        # Save all points to db
        self.save_all_points_db()

        # Convert to png and save as png and save to db
        Image.open("../../frontend-webapp/maps/" + self.name +
                   ".pgm").save("../../frontend-webapp/maps/" + self.name + ".png")
        self.database.add_map(self.name, "maps/" + self.name + ".png")

        rospy.loginfo("Map Creation phase complete!")

    def perform_localization(self):

        # Get template
        self.get_template()

        rospy.loginfo("Performing localization...")

        rospy.sleep(5)

        max_score, max_score_loc, rot_angle = localization.localize(
            self.map_path + ".pgm", self.template_path + ".pgm")

        rospy.loginfo("max_score: " + str(max_score))
        rospy.loginfo("location: " + str(max_score_loc))
        rospy.loginfo("angle: " + str(rot_angle))

        angle_rad = rot_angle * math.pi / 180

        rotation = pyquaternion.Quaternion(
            axis=[0.0, 0.0, 1.0], radians=angle_rad)

        quat = Quaternion(rotation[1], rotation[2], rotation[3], rotation[0])

        # Launch self navigation node
        os.system("gnome-terminal -x roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/darebalogun/Desktop/Turtlebot/turtlebot/frontend-webapp/maps/" + self.name + ".yaml")
        rospy.loginfo("Estimating Initial Pose...")
        rospy.sleep(3)

        # Publish location from localization back to rviz /initialpose
        pose_publisher = rospy.Publisher(
            "/initialpose", PoseWithCovarianceStamped, queue_size=10)
        poseWCS = PoseWithCovarianceStamped()
        poseWCS.header.frame_id = "map"
        poseWCS.header.stamp = rospy.Time.now()
        poseWCS.pose.pose.position.x = (
            max_score_loc[0] - self.map_size/2) * self.map_resolution
        poseWCS.pose.pose.position.y = -1 * \
            (max_score_loc[1] - self.map_size/2) * self.map_resolution
        poseWCS.pose.pose.position.z = 0
        poseWCS.pose.pose.orientation = quat
        poseWCS.pose.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]

        rate = rospy.Rate(1)
        pose_publisher.publish(poseWCS)
        rate.sleep()
        pose_publisher.publish(poseWCS)
        rate.sleep()
        pose_publisher.publish(poseWCS)

        # Publish markers on navigation node map
        self.add_marker_array()

    def perform_navigation(self):
        """
        Autonomous navigation to every position saved in self.positions
        """
        x = 0
        for position in self.positions:
            # TODO update quaternions
            success = self.navigator.goto(position, self.orientations[x])
            if success:
                rospy.loginfo("Hooray, reached the desired pose")
            else:
                rospy.loginfo("The base failed to reach the desired pose")

            # TODO Add image capture, processing and storage code here
            message_client.send("capture", self.name)
            # rospy.sleep(1)

            x = x + 1

        # TODO Add code to rename and transfer data
        message_client.send("save_all_images", self.name)

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

    def save_point(self, position, index):
        """
        Save point to database
        """
        # ROS coordinates have origin in centre of map, so we need to map to a coordinate system with origin in top left
        coordx = position['x']
        coordy = position['y']
        mappedx = position['x']/self.map_resolution + self.map_size/2
        mappedy = -1*position['y']/self.map_resolution + self.map_size/2

        # Add both sets of coordinates to database with image path
        # TODO get image path from camera capture module
        self.database.add_coordinate(
            self.name, coordx, coordy, "images/image" + str(index + 1) + ".jpg", mappedx, mappedy)

    def add_marker_array(self):
        """
        Add all markers
        """
        for position in self.positions:
            self.add_marker(position)

    def save_all_points_db(self):
        """
        Save all points to db
        """
        for index, position in enumerate(self.positions):
            self.save_point(position, index)

        rospy.loginfo("Points saved to database!")

    def get_template(self):
        """
        Get image of immediate surroundings
        """
        rospy.loginfo("Getting template...")
        StartRVIZ.start_rviz()

        time.sleep(8)

        rospy.loginfo("Saving Template...")
        os.system(
            "gnome-terminal -x rosrun map_server map_saver -f " + self.template_path)


if __name__ == '__main__':
    StartRVIZ.start_rviz()
    # os.system(
    #   "gnome-terminal --command='sh -c \"rostopic pub /reset std_msgs/Empty \"{}\"; PID=$!; sleep 1; kill $PID\"'")
    cmd = subprocess.Popen(
        ["rostopic pub /reset std_msgs/Empty \"{}\""], shell=True, stdout=subprocess.PIPE)
    mapname = raw_input("Please enter a name for the map: ")
    rospy.init_node('listener', anonymous=True)
    mappoints = MapPoints(mapname)
    mappoints.listener()
