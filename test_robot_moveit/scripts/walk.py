import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("Nours_publishing_node", anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()


#We create a DisplayTrajectory publisher which is used later to publish trajectories for RViz to visualize
display_trajectory_publisher = rospy.Publisher(
    "/move_group/display_planned_path",
    moveit_msgs.msg.DisplayTrajectory,
    queue_size=20,
)


## Getting Basic Information
# We can get the name of the reference frame for this robot:
# planning_frame = move_group.get_planning_frame()
# print("============ Planning frame: %s" % planning_frame)

# # We can also print the name of the end-effector link for this group:
# eef_link = move_group.get_end_effector_link()
# print("============ End effector link: %s" % eef_link)

# # We can get a list of all the groups in the robot:
# group_names = robot.get_group_names()
# print("============ Available Planning Groups:", robot.get_group_names())

# # Sometimes for debugging it is useful to print the entire state of the
# # robot:
# print("============ Printing robot state")
# print(robot.get_current_state())
# print("")

Legs_move_group = moveit_commander.MoveGroupCommander("Legs_group")

#returns an array of the groups' joint positions
Legs_joint_goal = Legs_move_group.get_current_joint_values()

print("----------Legs positions---------")
print(Legs_joint_goal)


Legs_joint_goal = [0,0,0,0,0,0,0,0]

#joint order
# 0- RHip_roll
# 1- RHip_pitch
# 2- RKnee_pitch
# 3- RAnkle_roll
# 4- LHip_roll
# 5- LHip_pitch
# 6- LKnee_pitch
# 7- LAnkle_roll


while not rospy.is_shutdown():
    #angles in radians
    Legs_joint_goal[4] = -0.057
    Legs_joint_goal[5] = -0.119
    Legs_joint_goal[6] = -Legs_joint_goal[5]
    Legs_joint_goal[7] = Legs_joint_goal[4]

    Legs_joint_goal[0] = -0.057
    Legs_joint_goal[1] = -0.172
    Legs_joint_goal[2] = -Legs_joint_goal[1]
    Legs_joint_goal[3] = Legs_joint_goal[0]
    Legs_move_group.go(Legs_joint_goal, wait=True)
    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    
    

    #angles in radians
    Legs_joint_goal[4] = 0.057
    Legs_joint_goal[5] = 0.172
    Legs_joint_goal[6] = -Legs_joint_goal[5]
    Legs_joint_goal[7] = Legs_joint_goal[4]
    

    Legs_joint_goal[0] = 0.057
    Legs_joint_goal[1] = 0.119
    Legs_joint_goal[2] = -Legs_joint_goal[1]
    Legs_joint_goal[3] = Legs_joint_goal[0]
    Legs_move_group.go(Legs_joint_goal, wait=True)
    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    
    

# Calling ``stop()`` ensures that there is no residual movement
Legs_move_group.stop()
