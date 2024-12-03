# Pre-requisites
1. Install ros
2. Install moveit `sudo apt install ros-noetic-moveit`
3. ros controllers `sudo apt install ros-noetic-ros-control ros-noetic-ros-controllers`

# Setup
1. Copy these package in the `/src` of your catkin workspace
2. go to your catkin workspace and run `catkin_make`
3. source the setup file using `source devel/setup.bash`

# How to use 
### Running the test robot in Gazebo
`roslaunch test_robot_urdf test_robot_urdf.launch`
### Running the test robot with Rviz and Moveit control
`roslaunch test_robot_moveit run_all.launch` 
Then run any script from `test_robot_moveit/scripts/` using `python3`

## Resources 
This project was largely based on this [playlist](https://www.youtube.com/playlist?list=PLeEzO_sX5H6TBD6EMGgV-qdhzxPY19m12) and [document](https://github.com/ageofrobotics/import_your_custom_urdf_package_to_ROS-main/blob/main/Importing_URDF_Package_from_Soloidworks_in_ROS.pdf) by [Age of robotics](https://github.com/ageofrobotics)
[Moveit documentation](https://moveit.github.io/moveit_tutorials/index.html)