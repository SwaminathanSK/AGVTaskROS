#!/usr/bin/env python3
import rclpy
import math
from rclpy.node import Node

import numpy as np
# TODO: include needed ROS msg type headers and libraries
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from ackermann_msgs.msg import AckermannDriveStamped, AckermannDrive


class SafetyNode(Node):
    """
    The class that handles emergency braking.
    """
    def __init__(self):
        super().__init__('safety_node')
        """
        One publisher should publish to the /drive topic with a AckermannDriveStamped drive message.

        You should also subscribe to the /scan topic to get the LaserScan messages and
        the /ego_racecar/odom topic to get the current speed of the vehicle.

        The subscribers should use the provided odom_callback and scan_callback as callback methods

        NOTE that the x component of the linear velocity in odom is the speed
        """
        self.speed = 0.
        self.publisher1 = self.create_publisher(AckermannDriveStamped, 'drive', 10)
        self.subscription1 = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.subscription1  # prevent unused variable warning
        self.subscription2 = self.create_subscription(
            Odometry,
            '/ego_racecar/odom',
            self.odom_callback,
            10)
        self.subscription2  # prevent unused variable warning

    def odom_callback(self, odom_msg):
        # update current speed
        self.speed = odom_msg.twist.twist.linear.x


    def scan_callback(self, scan_msg):
        minTTC = -1   
        # calculate TTC
        for i in scan_msg.ranges:
            if type(i) == float:
                _rate = (self.speed * (math.cos(scan_msg.angle_increment*i + (scan_msg.angle_min + scan_msg.angle_max)/2)))

                if _rate <= 0:
                    _rate = 0.0000001

                TTC = i/_rate
                if minTTC == -1:
                    minTTC = TTC
                elif TTC < minTTC:
                    minTTC = TTC
        
        # publish command to brake
        if minTTC < 1:
            self.get_logger().info('Publishing ackermann')
            ackermann_cmd_msg = AckermannDriveStamped()
            ackermann_cmd_msg.drive.speed = 0.
            ackermann_cmd_msg.drive.steering_angle = 0.
            self.publisher1.publish(ackermann_cmd_msg)
        pass

def main(args=None):
    rclpy.init(args=args)
    safety_node = SafetyNode()
    rclpy.spin(safety_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    safety_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()