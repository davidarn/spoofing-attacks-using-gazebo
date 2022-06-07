# Simulation of Sensor Spoofing Attacks on Quadcopters Using The Gazebo Simulator
Associated code of the work "Simulation of Sensor Spoofing Attacks on Quadcopters Using The Gazebo Simulator".

This repository provides the attack simulations implemented in the course of the work "Simulation of Sensor Spoofing Attacks on Quadcopters Using The Gazebo Simulator". Besides, the GNC framework utilized for this purpose is provided. Below is a description on how the implemented simulations can be utilized: 

## To execute the world used in the course of the work including the iris model equipped with the sensors described
To launch the world with Gazebo, on which the developments are based, as well as SITL and the associated ArduPilot framework. The described model is predefined with the corresponding sensors and components in order to perform the behaviour described in the work in a coherent manner. 
   ```
   $ roslaunch iq_sim runway.launch
   $ ./startsitl.sh
   $ roslaunch iq_sim apm.launch
   ```

## Execution of the control logic
The functionalities for evaluating the developed attack scenarios are executed as follows:

### Executing the obstacle avoidance logic
The logic that utilises the detection of obstacles in the environment via LiDAR to enable autonomous avoidance of those obstacles. The effect of LiDAR attacks can be analysed through this implemenation. 
   ```
   $ catkin_ws/src/iq_gnc/src$ rosrun iq_gnc obstacle_avoidance
   ``` 

### Execution of the waypoint logic
The logic that enables the autonomous control of defined waypoints based on the model's position data. The effect of LiDAR attacks can be evaluated based on this implementation. 
   ```
   $ catkin_ws/src/iq_gnc/src$ rosrun iq_gnc waypoints
   ``` 

## execution of the attacks

### Execution of the attacks on the LiDAR component
#### 1. Spoofing of the detection range
The requested distance values for spoofing the values observed by the LiDAR component are requested from the user. After a valid entry, the corresponding topic is spoofed. 
   ```
   $ catkin_ws/src/iq_gnc/scripts$ ./lidar_spoofing.py
   ``` 
  
#### 2. Jamming of the detection range
The script for jamming the recorded values of the LiDAR component with specified distance values is executed as follows. The range in which the distance values should be jammed is requested from the user by entering both a lower and an upper limit. After a valid input, random values within the resulting range are assigned for the distance values of the LiDAR component within the transmitted range. 
   ```
   $ catkin_ws/src/iq_gnc/scripts$ ./lidar_jamming.py
   ```

#### 3. Spooofing of a specific area within the detection range
A further attack scenario models an arbitrary obstacle by selectively spoofing parts of the LiDAR component's detection range with values within the threshold. This enables an attacker to gain control over the model. 
After invoking the script, the user can choose between the two different ranges described in the work after entering the value of the distance to be spoofed. 
   ```
   $ catkin_ws/src/iq_gnc/scripts$ ./lidar_front_obstacle.py
   ```

### Execution of the attacks on the odometry component
#### 1. Spoofing of the detection range
On invoking the script for spoofing the position data with arbitrary values, the user is requested to specify the desired values for the latitude and the longitude. The script manipulates the topic responsible for the global position data, which is further propagated to the local position data for the purpose of observing the effects in the simulation. 
   ```
   $ catkin_ws/src/iq_gnc/scripts$ ./gps_spoofing.py
   ``` 
  
#### 2. Jamming of the detection range
Upon invoking the script for jamming the position data with arbitrary values, the user is requested to provide information about the desired latitude and longitude. An upper and lower limit is defined for the pair of values. Subsequently, the coordinates are spoofed with random values within that range. 
   ```
   $ catkin_ws/src/iq_gnc/scripts$ ./gps_jamming.py
   ```

## License
[MIT](https://choosealicense.com/licenses/mit/)
