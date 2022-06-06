# Simulation of Sensor Spoofing Attacks on Quadcopters Using The Gazebo Simulator
Associated code of the work "Simulation of Sensor Spoofing Attacks on Quadcopters Using The Gazebo Simulator".

This repository provides the attack simulations implemented in the course of the work "Simulation of Sensor Spoofing Attacks on Quadcopters Using The Gazebo Simulator". Besides, the GNC framework utilized for this purpose is provided. Below is a description on how the implemented simulations can be utilized: 

## Ausführen der Beispielwelt der Arbeit mit dem Iris-Modell und den beschriebenen Sensoren
   ```
   $ catkin_ws/src $ ./lidar_spoofing
   $ npm install
   $ npm start
   ``` 

## Ausführen der Ansteuerungslogik
   ```
   $ roslaunch iq_sim runway.launch
   $ ./startsitl.sh
   $ roslaunch iq_sim apm.launch
   ``` 

### Ausführen der Obstacle Avoidance Logik
   ```
   $ catkin_ws/src/iq_gnc/src$ rosrun iq_gnc obstacle_avoidance
   ``` 

### Ausführen der Waypoint Logik
   ```
   $ catkin_ws/src/iq_gnc/src$ rosrun iq_gnc waypoints
   ``` 

## Ausführen der Attacken

### Ausführen der Attacken auf die LiDAR Komponente
#### 1. Spoofing des Erfassungsbereichs
   Das Skript zum Spoofen der erfassten Werte der LiDAR Komponente mit bestimmten Distanzwerten wird über das Terminal aufgerufen. Die gewünschten Distanzwerte werden vom User abgefragt. Nach einer gültigen Eingabe erfolgt das Spoofen des Topics. 
   enter distance to be spoofed
   ```
   $ catkin_ws/src/iq_gnc/scripts$ ./lidar_spoofing.py
   ``` 
  
#### 2. Jamming des Erfassungsbereichs
   Das Skript zum Jammen der erfassten Werte der LiDAR Komponente mit bestimmten Distanzwerten wird über das Terminal aufgerufen. Der Bereich, in dem die Distanzwerte gejammed werden sollen, werden vom User abgefragt. Nach einer gültigen Eingabe erfolgt das Zuweisen zufälliger Werte für dei Distanzwerte der LiDAR Komponente innerhalb des übermittelten Bereichs. 
   enter lower and upper limit
   ```
   $ catkin_ws/src/iq_gnc/scripts$ ./lidar_jamming.py
   ```

#### 3. Spoofen von einem bestimmten Bereich des Erfassungsbereichs
   Das Skript 
   enter the distance for an arbitrary obstacle the lidar has to be spoofed with and select range 1 or 2
   ```
   $ catkin_ws/src/iq_gnc/scripts$ ./lidar.py
   ```

### Ausführen der Attacken auf die Odometry Komponente
#### 1. Spoofing des Erfassungsbereichs
   Das Skript zum Spoofen der erfassten Werte der LiDAR Komponente mit bestimmten Distanzwerten wird über das Terminal aufgerufen. Die gewünschten Distanzwerte werden vom User abgefragt. Nach einer gültigen Eingabe erfolgt das Spoofen des Topics. 
   latitude and longitude eingeben
   ```
   $ catkin_ws/src/iq_gnc/scripts$ ./gps_spoofing.py
   ``` 
  
#### 2. Jamming des Erfassungsbereichs
   Das Skript zum Jammen der erfassten Werte der LiDAR Komponente mit bestimmten Distanzwerten wird über das Terminal aufgerufen. Der Bereich, in dem die Distanzwerte gejammed werden sollen, werden vom User abgefragt. Nach einer gültigen Eingabe erfolgt das Zuweisen zufälliger Werte für dei Distanzwerte der LiDAR Komponente innerhalb des übermittelten Bereichs. 
   lowre and upper limit jeweils latitude und longitude
   ```
   $ catkin_ws/src/iq_gnc/scripts$ ./gps_jamming.py
   ```

## License
[MIT](https://choosealicense.com/licenses/mit/)
