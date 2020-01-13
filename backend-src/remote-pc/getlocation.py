import rospy
from nav_msgs.msg import Odometry


class Location:
    def __init__(self):
        rospy.init_node('get_location', anonymous=True)
        self.sub = rospy.Subscriber("odom", Odometry, self.callback)
        rospy.spin()

    def callback(self, data):
        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y
