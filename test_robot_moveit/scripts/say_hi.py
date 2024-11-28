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

Rarm_move_group = moveit_commander.MoveGroupCommander("Rarm_group")
#returns an array of the groups' joint positions
Rarm_joint_goal = Rarm_move_group.get_current_joint_values()
print("\n\n", Rarm_joint_goal, "\n\n")

while not rospy.is_shutdown():
    #angles in radians
    Rarm_joint_goal[0] = -3
    Rarm_joint_goal[1] = 0.5
    Rarm_joint_goal[2] = 0

    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    Rarm_move_group.go(Rarm_joint_goal, wait=True)

    #angles in radians
    Rarm_joint_goal[0] = -3
    Rarm_joint_goal[1] = 0.0
    Rarm_joint_goal[2] = 0

    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    Rarm_move_group.go(Rarm_joint_goal, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
Rarm_move_group.stop()