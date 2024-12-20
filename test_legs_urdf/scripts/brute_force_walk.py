import rospkg
import rospy
from std_msgs.msg import Float64
import time
import math

#ros topics

# Publisher_name = rospy.Publisher('topic_name', msg_type, queue_size=5)

# Angles publishers
RAnkle_roll_pub = rospy.Publisher('/RAnkle_roll_position_controller/command', Float64, queue_size=5)
RAnkle_pitch_pub= rospy.Publisher('/RAnkle_pitch_position_controller/command', Float64, queue_size=5)
RKnee_pitch_pub = rospy.Publisher('/RKnee_pitch_position_controller/command', Float64, queue_size=5)
RHip_pitch_pub  = rospy.Publisher('/RHip_pitch_position_controller/command', Float64, queue_size=5)
RHip_roll_pub   = rospy.Publisher('/RHip_roll_position_controller/command', Float64, queue_size=5)
RHip_yaw_pub    = rospy.Publisher('/RHip_yaw_position_controller/command', Float64, queue_size=5)

LAnkle_roll_pub = rospy.Publisher('/LAnkle_roll_position_controller/command', Float64, queue_size=5)
LAnkle_pitch_pub= rospy.Publisher('/LAnkle_pitch_position_controller/command', Float64, queue_size=5)
LKnee_pitch_pub = rospy.Publisher('/LKnee_pitch_position_controller/command', Float64, queue_size=5)
LHip_pitch_pub  = rospy.Publisher('/LHip_pitch_position_controller/command', Float64, queue_size=5)
LHip_roll_pub   = rospy.Publisher('/LHip_roll_position_controller/command', Float64, queue_size=5)
LHip_yaw_pub    = rospy.Publisher('/LHip_yaw_position_controller/command', Float64, queue_size=5)



#defining node
rospy.init_node('Nours_sad_publishing_node', anonymous=False)
rate = rospy.Rate(10) # Hz 



def walk_X_steps(steps=0):

    #first step is to shift weight to one leg
    LAnkle_roll = -0.17 #rad
    RAnkle_roll = LAnkle_roll

    RHip_roll   = -RAnkle_roll
    LHip_roll   = -LAnkle_roll

    print("Shifting weight")
    LAnkle_roll_pub.publish(LAnkle_roll)
    LHip_roll_pub.publish(LHip_roll)
    RAnkle_roll_pub.publish(RAnkle_roll)
    RHip_roll_pub.publish(RHip_roll)

    time.sleep(4)
    #second step is to lift the leg that isnt holding the weight
    print("Rasising leg")
    LAnkle_pitch = -0.15 #rad
    LKnee_pitch = -0.016 * LAnkle_pitch**2 - 0.65
    LHip_pitch  = -3*LAnkle_pitch + 0.4

    LHip_pitch_pub.publish(LHip_pitch)
    LKnee_pitch_pub.publish(LKnee_pitch)
    LAnkle_pitch_pub.publish(LAnkle_pitch)


    
    #Time for our favourite inverted while shifting weight
    print("Shifting weight")
    RAnkle_pitch = -0.6
    RKnee_pitch = -0.016 * RAnkle_pitch**2 + 0.65
    RHip_pitch = -0.1*RAnkle_pitch - 0.4

    LAnkle_roll = 0.17 #rad
    RAnkle_roll = LAnkle_roll

    RHip_roll   = -RAnkle_roll
    LHip_roll   = -LAnkle_roll

     
    RAnkle_pitch_pub.publish(RAnkle_pitch)
    RHip_pitch_pub.publish(RHip_pitch)
    RKnee_pitch_pub.publish(RKnee_pitch)
    time.sleep(2)
    LAnkle_roll_pub.publish(LAnkle_roll)
    LHip_roll_pub.publish(LHip_roll)
    RAnkle_roll_pub.publish(RAnkle_roll)
    RHip_roll_pub.publish(RHip_roll)
    
    
    print("------Done------\n")





#golden ratios
#angles msgs in rad
#These numbers are for standing up and ready to move
LAnkle_roll = 0.0
LAnkle_pitch= 0.233
LKnee_pitch = -0.016 * LAnkle_pitch**2 - 0.65
LHip_pitch  = LAnkle_pitch + 0.167
LHip_roll   = -LAnkle_roll
LHip_yaw    = 0.0


RAnkle_roll = 0.0
RAnkle_pitch= -0.233
RKnee_pitch = -0.016 * RAnkle_pitch**2 + 0.65
RHip_pitch  = RAnkle_pitch - 0.167
RHip_roll   = -RAnkle_roll
RHip_yaw    = 0.0

# just a function to calculate the angles for me
# instead of writing the equations every time
def calculate():
    global RAnkle_roll 
    global RAnkle_pitch
    global RKnee_pitch 
    global RHip_pitch  
    global RHip_roll   
    global RHip_yaw 

    global LAnkle_roll 
    global LAnkle_pitch
    global LKnee_pitch 
    global LHip_pitch  
    global LHip_roll   
    global LHip_yaw 

    RKnee_pitch = -0.016 * RAnkle_pitch**2 + 0.65
    RHip_pitch  = RAnkle_pitch - 0.167
    RHip_roll   = -RAnkle_roll

    LKnee_pitch = -0.016 * LAnkle_pitch**2 - 0.65
    LHip_pitch  = LAnkle_pitch + 0.167
    LHip_roll   = -LAnkle_roll   
    

RAnkle_roll_pub.publish(RAnkle_roll)
RAnkle_pitch_pub.publish(RAnkle_pitch)
#RKnee_pitch_pub.publish(RKnee_pitch)
RHip_pitch_pub.publish(RHip_pitch)
RHip_roll_pub.publish(RHip_roll)
#RHip_yaw_pub.publish(RHip_yaw)

LAnkle_roll_pub.publish(LAnkle_roll)
LAnkle_pitch_pub.publish(LAnkle_pitch)
#LKnee_pitch_pub.publish(LKnee_pitch)
LHip_pitch_pub.publish(LHip_pitch)
LHip_roll_pub.publish(LHip_roll)
#LHip_yaw_pub.publish(LHip_yaw)




while not rospy.is_shutdown():

    #input("Start? ")
    #walk_X_steps()

    #first step is to shift weight to one leg
    LAnkle_roll = float(input("LAnkle_roll: "))#-0.17 rad
    RAnkle_roll = LAnkle_roll

    calculate()

    LAnkle_roll_pub.publish(LAnkle_roll)
    LHip_roll_pub.publish(LHip_roll)
    RAnkle_roll_pub.publish(RAnkle_roll)
    RHip_roll_pub.publish(RHip_roll)


    #second step is to lift the leg that isnt holding the weight
    LAnkle_pitch = float(input("LAnkle_pitch: "))#-0.2 rad
    LKnee_pitch = -0.016 * LAnkle_pitch**2 - 0.65
    LHip_pitch  = -3*LAnkle_pitch + 0.4

    if LAnkle_pitch == 0.0:
        #initial positions
        LAnkle_pitch_pub.publish(0.233)
        LKnee_pitch_pub.publish(LKnee_pitch)
        LHip_pitch_pub.publish(LHip_pitch)
    else:
        LHip_pitch_pub.publish(LHip_pitch)
        LKnee_pitch_pub.publish(LKnee_pitch)
        LAnkle_pitch_pub.publish(LAnkle_pitch)



    #Time for our favourite inverted 
    RAnkle_pitch = float(input("RAnkle_pitch: "))
    RKnee_pitch = -0.016 * RAnkle_pitch**2 + 0.65
    RHip_pitch = -0.1*RAnkle_pitch - 0.4

    if RAnkle_pitch == 0.0:
        RAnkle_pitch_pub.publish(-0.233)
    else:   
        RAnkle_pitch_pub.publish(RAnkle_pitch)
        RHip_pitch_pub.publish(RHip_pitch)
        RKnee_pitch_pub.publish(RKnee_pitch)
    

    print("------Done------\n")