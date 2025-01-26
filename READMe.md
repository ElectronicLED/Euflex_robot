
## 0. Pre-requisites

Before starting, make sure you have the following installed:

1. **ROS** (Robot Operating System)
2. **MoveIt**: Install using the following command:
   ```
   sudo apt install ros-noetic-moveit
   ```
3. **ROS Controllers**: Install using the following command:
   ```
   sudo apt install ros-noetic-ros-control ros-noetic-ros-controllers
   ```

## 1. Setup

Follow these steps to set up the project:

1. **Copy the packages** into the `/src` folder of your catkin workspace.
2. **Build the workspace**:
   ```
   cd ~/your_catkin_ws
   catkin_make
   ```
3. **Source the setup file**:
   ```
   source devel/setup.bash
   ```

## 2. How to Use

### Running the Test Robot

**Important:** Set the Physics Engine’s Error Reduction Parameter (ERP) to `0.02` for the simulation to run smoothly.

You can launch the test robot in two different ways:

1. **With Gazebo**:
   ```
   roslaunch test_robot_urdf test_robot_urdf.launch
   ```

2. **With Rviz and MoveIt Control**:
   ```
   roslaunch test_robot_moveit run_all.launch
   ```

After launching, you can run any script from the `test_robot_moveit/scripts/` folder by executing:
   ```
   python3 <script_name>.py
   ```

### Running the Test Legs

To run the simulation and publish joint positions:

1. Launch the simulation:
   ```
   roslaunch test_legs_urdf position_leg.launch
   ```

2. Then, use `python3` to run either script from the `scripts` folder:
   ```
   python3 <script_name>.py
   ```

### Running the Legs with MoveIt and Rviz

For MoveIt and Rviz integration with trajectory controllers:

1. **Edit the URDF**: Uncomment the trajectory controllers and comment the effort controllers.
2. **Launch the simulation with MoveIt and Rviz**:
   ```
   roslaunch test_legs_moveit legs.launch
   ```

_moveit packages comes with a `scripts` folder for publishing joint movements. To use them launch the package with Rviz and Moveit then simply use python3 to run the desired script. However, **it is recommended to use C++** for more efficient handling, as MoveIt’s Python functionality is limited.

## 3. Resources

### 3.1 Tools

The project is built based on the following resources:

- [Age of Robotics YouTube Playlist](https://www.youtube.com/playlist?list=PLeEzO_sX5H6TBD6EMGgV-qdhzxPY19m12)
- [Importing URDF Package from SolidWorks in ROS - GitHub Guide](https://github.com/ageofrobotics/import_your_custom_urdf_package_to_ROS-main/blob/main/Importing_URDF_Package_from_Soloidworks_in_ROS.pdf)
- [MoveIt Documentation](https://moveit.github.io/moveit_tutorials/index.html)
- [Original Test Robot Design on GrabCAD](https://grabcad.com/library/humanoid-robot-14)
- [pySLAM](https://github.com/luigifreda/pyslam)
- [VINS-MONO](https://github.com/HKUST-Aerial-Robotics/VINS-Mono)
- [rtabmap](https://wiki.ros.org/rtabmap_ros)

### 3.2 Theory

For a deeper understanding of humanoid robots, consider exploring the following resources:

- **Jessy W. Grizzle’s Lecture on Bipedal Robots**: [Watch here](https://www.youtube.com/watch?v=EMX7wc0vcWE)
- **Introduction to Humanoid Robots** by Shuuji Kajita, Hirohisa Hirukawa, Kensuke Harada, and Kazuhito Yokoi.
- **SLAM Course** by Cyrill Stachniss [here](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_).

---