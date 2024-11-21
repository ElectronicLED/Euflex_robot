## Prerequisite
1. gazebo_ros_pkgs
2. moveit ```sudo apt install ros-noetic-moveit```
3. join-trajectory-controller ```sudo apt-get install ros-noetic-joint-trajectory-controller```

## How to use
1. Copy these packages to your_catkin_workspace/src
2. Build your workspace using `catkin_make`
3. Source the setup `source your_catkin_workspace/devel/setup.bash`
4. Try and run the test packages using `roslaunch test_robot_moveit run_all.launch`

## Resources 
This project is hugely based on this amazing [Playlist](https://youtube.com/playlist?list=PLeEzO_sX5H6TBD6EMGgV-qdhzxPY19m12&si=qwMbpVgd27WaYGel) and [Document](https://github.com/ageofrobotics/import_your_custom_urdf_package_to_ROS-main/blob/main/Importing_URDF_Package_from_Soloidworks_in_ROS.pdf) by [Age of Robotics](https://github.com/ageofrobotics)
