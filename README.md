# indoorView
IndoorView is a Google StreetView Experience for indoor spaces. The systems includes using a robotic platform used to map a space and capture 360 degree images and a user facing web application to host the interactive map. This project is the 4th year engineering and design capstone project in the Systems and Computer Engineering department at Carleton University

### Group Members
Dare Balogun  
Gregory Koloniaris  
Emad Arid  
Zoya Mushtaq  
Anannya Bhatia  

### Supervising Professor
Dr. Mohamed Atia

### Deployment
This project is currently deployed on heroku [here](https://cu-indoorview.herokuapp.com/)

## Getting Started
The following instructions will show you how to get the system running and how to capture a map and host on the web

### Prerequisites
* TurtleBot 3 Burger
* PC running Ubuntu 16.04 xenial with python2.7
* Ricoh Theta S
* Joystick controller (optional)

### Instructions
1. Complete TurtleBot setup and Install ROS on your PC by following instructions [here](http://emanual.robotis.com/docs/en/platform/turtlebot3/setup/)

2. Clone this repository on your PC and cd into backend-src/remote-pc
```
(PC) $ git clone https://github.com/darebalogun/indoorView.git
(PC) $ cd indoorView/backend-src/remote-pc
```

3. Ensure the PC and the TurtleBot Raspberry Pi are connected to the same network

4. Run NetworkConfig.py to perform network configuration on the PC. Note the IP address of the PC
```
(PC) $ python NetworkConfigPC.py
```

5. Start roscore server (in another terminal)
```
(PC) $ source ~/.bashrc
(PC) $ roscore
```

6. If using the optional joystick PC controller, connect it to your PC now

7. Copy folder turtlebot-pi onto the TurtleBot Raspberry Pi

8. Cd into that folder on the Raspberry PI and perform network config by filling in the IP address of PC from step 4 (ctrl-X then Y to save) and running NetworkConfig.py
```
(Pi) $ nano NetworkConfigRPi.py
(Pi) $ python NetworkConfigRPi.py
```

9. Run startup.sh
```
(Pi) $ source ./startup.sh
```

10. Place the TurtleBot in the middle of the room on the floor where its able to navigate around the room

11. Open savetodatabase.py and configure database parameters

12. Run mappoints.py then enter a name for the map
```
(PC) $ python mappoints.py
Please enter a name for the map: [map_name]
```

13. Navigate the robot around the area using the controller or using the keyboard. To use keyboard follow instructions [here](http://emanual.robotis.com/docs/en/platform/turtlebot3/teleoperation/#keyboard)

14. Once the area is fully mapped, click publish point at the top of the RVIZ window then click on points of interest on the map.
    The map will autogenerate intermediary points spaced 0.5m apart

15. Go back to the terminal window running mappoints and press enter when done

16. A new RVIZ navigation window should pop up. [Estimate the initial pose](http://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#estimate-initial-pose)
    1. Click 2D Pose Estimate near the top of the window
    2. Click (and hold) on the approximate location of the robot on the map 
    3. Align the green arrow with the approximate orientation of the robot on the map
    4. Move the robot back and forth a few times to align the map with SLAM information

17. Return to the terminal window and press enter when done. The robot should navigate autonomously to the chosen points and capture images for the map

18. Point co-ordinates and location of images should now be saved to the database

### TO-DO
1. ~Add config file with:~ 
    1. ~Map size~
    2. ~Map resolution~
    3. ~Photo spacing~
2. ~Quarternion calculations~
3. ~Start point from current location of robot~
4. Remove file structure naming pertinent to my pc
5. More user friendly CLI
6. Update Readme with config file steps
7. ~Update menu in html pages~
8. ~Fix auto-increment ID bug in database~
9. ~Reduce max velocity for stability~
10. Fix map coordinates size and positions
11. Clean up folder structure on PI
