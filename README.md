# Simulation of Sensor Spoofing Attacks on Quadcopters Using The Gazebo Simulator
Associated code of the work "Simulation of Sensor Spoofing Attacks on Quadcopters Using The Gazebo Simulator".

This repository provides the attack simulations implemented in the course of the work "Simulation of Sensor Spoofing Attacks on Quadcopters Using The Gazebo Simulator". Besides, the GNC framework utilized for this purpose is provided. Below is a description on how the implemented simulations can be utilized: 

## Ausführen der Beispielwelt der Arbeit mit dem Iris-Modell und den beschriebenen Sensoren

## Ausführen der Ansteuerungslogik

### Ausführen der Obstacle Avoidance Logik

### Ausführen der Waypoint Logik

## Ausführen der Attacken

### Ausführen der Attacken auf die LiDAR Komponente
#### 1. Spoofing des Erfassungsbereichs
   Das Skript zum Spoofen der erfassten Werte der LiDAR Komponente mit bestimmten Distanzwerten wird über das Terminal aufgerufen. Die gewünschten Distanzwerte werden vom User abgefragt. Nach einer gültigen Eingabe erfolgt das Spoofen des Topics. 
   ```
   $ catkin_ws/src $ ./lidar_spoofing
   $ npm install
   $ npm start
   ``` 
  
#### 2. Jamming des Erfassungsbereichs
   Das Skript zum Jammen der erfassten Werte der LiDAR Komponente mit bestimmten Distanzwerten wird über das Terminal aufgerufen. Der Bereich, in dem die Distanzwerte gejammed werden sollen, werden vom User abgefragt. Nach einer gültigen Eingabe erfolgt das Zuweisen zufälliger Werte für dei Distanzwerte der LiDAR Komponente innerhalb des übermittelten Bereichs. 
   ```
   $ catkin_ws/src $ ./lidar_spoofing
   $ npm install
   $ npm start
   ```

#### 3. Spoofen von einem bestimmten Bereich des Erfassungsbereichs
   Das Skript 
   ```
   $ catkin_ws/src $ ./lidar_spoofing
   $ npm install
   $ npm start
   ```

### Ausführen der Attacken auf die Odometry Komponente
#### 1. Spoofing des Erfassungsbereichs
   Das Skript zum Spoofen der erfassten Werte der LiDAR Komponente mit bestimmten Distanzwerten wird über das Terminal aufgerufen. Die gewünschten Distanzwerte werden vom User abgefragt. Nach einer gültigen Eingabe erfolgt das Spoofen des Topics. 
   ```
   $ catkin_ws/src $ ./lidar_spoofing
   $ npm install
   $ npm start
   ``` 
  
#### 2. Jamming des Erfassungsbereichs
   Das Skript zum Jammen der erfassten Werte der LiDAR Komponente mit bestimmten Distanzwerten wird über das Terminal aufgerufen. Der Bereich, in dem die Distanzwerte gejammed werden sollen, werden vom User abgefragt. Nach einer gültigen Eingabe erfolgt das Zuweisen zufälliger Werte für dei Distanzwerte der LiDAR Komponente innerhalb des übermittelten Bereichs. 
   ```
   $ catkin_ws/src $ ./lidar_spoofing
   $ npm install
   $ npm start
   ```

## License
[MIT](https://choosealicense.com/licenses/mit/)
