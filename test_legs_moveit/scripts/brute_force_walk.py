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

# Sometimes for debugging it is useful to print the entire state of the
# # robot:
# print("============ Printing robot state")
# print(robot.get_current_state())
# print("")

Legs_move_group = moveit_commander.MoveGroupCommander("legs_move_group")

# #returns an array of the groups' joint positions
# Legs_joint_goal = Legs_move_group.get_current_joint_values()

# print("----------Legs positions---------")
# print(Legs_joint_goal)


# Joint order:
#0 - LHip_yaw
#1 - LHip_roll
#2 - LHip_pitch
#3 - LKnee_pitch
#4 - LAnkle_pitch
#5 - LAnkle_roll
#6 - RHip_yaw
#7 - RHip_roll
#8 - RHip_pitch
#9 - RKnee_pitch
#10- RAnkle_pitch
#11- RAnkle_roll

def StepForward(steps):

    for i in range(steps):
        #angles are in radian
        LHip_yaw    = 0.8
        LHip_roll   = 0.0
        LHip_pitch  = 0.0
        LKnee_pitch = 0.0
        LAnkle_pitch= 0.0
        LAnkle_roll = LHip_roll

        RHip_yaw    = 0.8
        RHip_roll   = 0.0
        RHip_pitch  = 0.0
        RKnee_pitch = 0.0
        RAnkle_pitch= 0.0
        RAnkle_roll = RHip_roll

        Legs_joint_goal = [LHip_yaw, LHip_roll, LHip_pitch, LKnee_pitch, LAnkle_pitch, LAnkle_roll,
                        RHip_yaw, RHip_roll, RHip_pitch, RKnee_pitch, RAnkle_pitch, RAnkle_roll ]
        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        Legs_move_group.go(Legs_joint_goal, wait=True)



        #angles are in radian
        LHip_yaw    = 0.0
        LHip_roll   = 0.0
        LHip_pitch  = 0.0
        LKnee_pitch = 0.0
        LAnkle_pitch= 0.0
        LAnkle_roll = LHip_roll

        RHip_yaw    = 0.0
        RHip_roll   = 0.0
        RHip_pitch  = 0.0
        RKnee_pitch = 0.0
        RAnkle_pitch= 0.0
        RAnkle_roll = RHip_roll

        Legs_joint_goal = [LHip_yaw, LHip_roll, LHip_pitch, LKnee_pitch, LAnkle_pitch, LAnkle_roll,
                        RHip_yaw, RHip_roll, RHip_pitch, RKnee_pitch, RAnkle_pitch, RAnkle_roll ]
        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        Legs_move_group.go(Legs_joint_goal, wait=True)




#angles are in radian
LAnkle_roll = 0.0
LAnkle_pitch= 0.233
LKnee_pitch = -0.602
LHip_pitch  = LAnkle_pitch + 0.167
LHip_roll   = LAnkle_roll
LHip_yaw    = 0.0


RAnkle_roll = 0.0
RAnkle_pitch= -0.233
RKnee_pitch = 0.602
RHip_pitch  = RAnkle_pitch - 0.167
RHip_roll   = RAnkle_roll
RHip_yaw    = 0.0




Legs_joint_goal = [LHip_yaw, LHip_roll, LHip_pitch, LKnee_pitch, LAnkle_pitch, LAnkle_roll,
                   RHip_yaw, RHip_roll, RHip_pitch, RKnee_pitch, RAnkle_pitch, RAnkle_roll ]
# The go command can be called with joint values, poses, or without any
# parameters if you have already set the pose or joint target for the group
Legs_move_group.go(Legs_joint_goal, wait=True)





#while not rospy.is_shutdown():

    
    
    
    
    
    

    
    
    
    

# Calling ``stop()`` ensures that there is no residual movement
Legs_move_group.stop()
