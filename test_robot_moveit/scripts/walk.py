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

Lleg_move_group = moveit_commander.MoveGroupCommander("Lleg_group")
Rleg_move_group = moveit_commander.MoveGroupCommander("Rleg_group")
#returns an array of the groups' joint positions
# Lleg_joint_goal = Lleg_move_group.get_current_joint_values()
# Rleg_joint_goal = Rleg_move_group.get_current_joint_values()
Lleg_joint_goal = [0,0,0,0]
Rleg_joint_goal = [0,0,0,0]

while not rospy.is_shutdown():
    #angles in radians
    Lleg_joint_goal[0] = 0.057
    Lleg_joint_goal[1] = 0.119
    Lleg_joint_goal[2] = -Lleg_joint_goal[1]
    Lleg_joint_goal[3] = Lleg_joint_goal[0]
    Lleg_move_group.go(Lleg_joint_goal, wait=True)

    Rleg_joint_goal[0] = 0.057
    Rleg_joint_goal[1] = -0.172
    Rleg_joint_goal[2] = -Rleg_joint_goal[1]
    Rleg_joint_goal[3] = Rleg_joint_goal[0]
    Rleg_move_group.go(Rleg_joint_goal, wait=True)
    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    
    

    #angles in radians
    Lleg_joint_goal[0] = 0.057
    Lleg_joint_goal[1] = -0.172
    Lleg_joint_goal[2] = -Lleg_joint_goal[1]
    Lleg_joint_goal[3] = Lleg_joint_goal[0]
    Lleg_move_group.go(Lleg_joint_goal, wait=True)

    Rleg_joint_goal[0] = 0.057
    Rleg_joint_goal[1] = 0.119
    Rleg_joint_goal[2] = -Rleg_joint_goal[1]
    Rleg_joint_goal[3] = Rleg_joint_goal[0]
    Rleg_move_group.go(Rleg_joint_goal, wait=True)
    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    
    

# Calling ``stop()`` ensures that there is no residual movement
Lleg_move_group.stop()
Rleg_move_group.stop()