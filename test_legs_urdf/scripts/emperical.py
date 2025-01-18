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



l1 = 0.053  # Length of first link (m)
l2 = 0.079    # Length of second link (m)



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
#angles msgs are in rad
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



def neutralPosition(Leg="LR"):
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

    if Leg == "L" or Leg == "LR":
        LAnkle_roll = 0.0
        LAnkle_pitch= 0.233
        LKnee_pitch = -0.016 * LAnkle_pitch**2 - 0.65
        LHip_pitch  = LAnkle_pitch + 0.19
        LHip_roll   = -LAnkle_roll
        LHip_yaw    = 0.0

        LAnkle_roll_pub.publish(LAnkle_roll)
        LAnkle_pitch_pub.publish(LAnkle_pitch)
        LKnee_pitch_pub.publish(LKnee_pitch)
        LHip_pitch_pub.publish(LHip_pitch)
        LHip_roll_pub.publish(LHip_roll)
        LHip_yaw_pub.publish(LHip_yaw)
    
    if Leg == "R" or Leg == "LR":
        RAnkle_roll = 0.0
        RAnkle_pitch= -0.233
        RKnee_pitch = -0.016 * RAnkle_pitch**2 + 0.65
        RHip_pitch  = RAnkle_pitch - 0.19
        RHip_roll   = -RAnkle_roll
        RHip_yaw    = 0.0 

        RAnkle_roll_pub.publish(RAnkle_roll)
        RAnkle_pitch_pub.publish(RAnkle_pitch)
        RKnee_pitch_pub.publish(RKnee_pitch)
        RHip_pitch_pub.publish(RHip_pitch)
        RHip_roll_pub.publish(RHip_roll)
        RHip_yaw_pub.publish(RHip_yaw)

    





while not rospy.is_shutdown():

    #walk_X_steps()
    while True:
        if input("Start? ") == 'y':
            time.sleep(1)
            break
        if input("Reset? ") == 'y':
            neutralPosition()
            print("Reseting...")
            time.sleep(5)
        

    # 1- first step is to shift weight to one leg
    # LAnkle_roll = float(input("LAnkle_roll: "))#-0.17 rad
    LAnkle_roll = -0.17
    LHip_roll   = -LAnkle_roll 

    RAnkle_roll = LAnkle_roll
    RHip_roll   = -RAnkle_roll

    LAnkle_roll_pub.publish(LAnkle_roll)
    LHip_roll_pub.publish(LHip_roll)
    RAnkle_roll_pub.publish(RAnkle_roll)
    RHip_roll_pub.publish(RHip_roll)





    time.sleep(1)
    # 2- second step is to lift the leg that isnt holding the weight
    '''LAnkle_pitch = float(input("LAnkle_pitch: "))#-0.2 rad
    LKnee_pitch = -0.016 * LAnkle_pitch**2 - 0.65
    LHip_pitch  = -3*LAnkle_pitch + 0.4'''
    #LHip_pitch = float(input("LHip_pitch: "))
    #LKnee_pitch = float(input("LKnee_pitch: "))
    LHip_pitch = 0.2
    LKnee_pitch = 0.2
    LAnkle_pitch = - LKnee_pitch - LHip_pitch

    #يعني معنضبجش
    foot_y = (l1+l2*math.cos(LKnee_pitch))*math.sin(LHip_pitch)
    foot_height = (l1+l2) - (l1+l2*math.cos(LKnee_pitch))*math.cos(LHip_pitch)
    #print(f"Height: {foot_height},  Y:{foot_y}")    
    

    if LHip_pitch == 0.0 :
        neutralPosition('L')
    else:
        LHip_pitch_pub.publish(LHip_pitch)
        LKnee_pitch_pub.publish(LKnee_pitch)
        LAnkle_pitch_pub.publish(LAnkle_pitch)



    for i in range(5):
        print(i)
        time.sleep(1)
    # 3- Time for our favourite inverted pendulum
    RAnkle_pitch = float(input("RAnkle_pitch: "))
    RKnee_pitch = -0.016 * RAnkle_pitch**2 + 0.65
    RHip_pitch = -0.1*RAnkle_pitch - 0.4

    LHip_pitch = 0.2 - RHip_pitch
    LKnee_pitch = 0.2
    LAnkle_pitch = - LKnee_pitch - LHip_pitch - LAnkle_pitch

    if RAnkle_pitch == 0.0:
        RAnkle_pitch_pub.publish(-0.233)
    else:   
        RAnkle_pitch_pub.publish(RAnkle_pitch)
        RHip_pitch_pub.publish(RHip_pitch)
        RKnee_pitch_pub.publish(RKnee_pitch)

        LHip_pitch_pub.publish(LHip_pitch)
        LKnee_pitch_pub.publish(LKnee_pitch)
        LAnkle_pitch_pub.publish(LAnkle_pitch)





    
    # Third Experimental step is to lower the raised leg from the hip to begin the weight shift
    time.sleep(3)
    #RHip_roll = float(input("RHip_roll: ")) # 0.3
    RHip_roll = 0.3


    if RHip_roll == 0:
        LAnkle_roll = -0.17
        LHip_roll   = -LAnkle_roll 
        RAnkle_roll = LAnkle_roll
        RHip_roll   = -RAnkle_roll
    else:
        LHip_roll = RHip_roll
        LAnkle_roll = -LHip_roll

    LHip_roll_pub.publish(LHip_roll)
    RAnkle_roll_pub.publish(RAnkle_roll)
    RHip_roll_pub.publish(RHip_roll)


   
    '''
    time.sleep(5)
    # Shift the weight to the front leg
    LAnkle_roll = 0.17
    LHip_roll   = -LAnkle_roll 

    RAnkle_roll = LAnkle_roll
    RHip_roll   = -RAnkle_roll

    LAnkle_roll_pub.publish(LAnkle_roll)
    LHip_roll_pub.publish(LHip_roll)
    RAnkle_roll_pub.publish(RAnkle_roll)
    RHip_roll_pub.publish(RHip_roll)'''


    
    

    print("------Done------\n")