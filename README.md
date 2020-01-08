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

## Getting Started
The following instructions will show you how to get the system running and how to capture a map and host on the web

### Prerequisites
* TurtleBot 3 Burger
* PC running Ubuntu 16.04 xenial with python2.7
* Ricoh Theta S
* Joystick controller (optional)

### Instructions
Complete TurtleBot setup and Install ROS on your PC by following instructions [here](http://emanual.robotis.com/docs/en/platform/turtlebot3/setup/)

Clone this repository on your PC and cd into it
```
git clone https://github.com/darebalogun/indoorView.git
cd indoorView
```

If using the optional joystick PC controller, connect it to your PC now

Launch SLAM node in RVIZ
```
python StartRVIZ
```

Navigate the robot around the area using the controller or using the keyboard. To use keyboard follow instructions [here](http://emanual.robotis.com/docs/en/platform/turtlebot3/teleoperation/#keyboard)

Once the area is fully mapped, run savepoints.py
```
python savepoints.py
```

