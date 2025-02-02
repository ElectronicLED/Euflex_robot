import rospkg
import rospy
from std_msgs.msg import Float64
import time
import math

#ros topics
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

    while True:
        if input("Start? ") == 'y':
            time.sleep(1)
            print("")
            break
        if input("Reset? ") == 'y':
            neutralPosition()
            print("Reseting...")
            time.sleep(5)
        if input("End Script? ") == 'y':
            quit()
        

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
    #LHip_pitch = float(input("LHip_pitch: "))
    #LKnee_pitch = float(input("LKnee_pitch: "))
    print("Lifting leg..")
    LHip_pitch = LHip_pitch + 0.2
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



    
    time.sleep(3)
    print("Back leg inverted pendelum...")
    # 3- Time for our favourite inverted pendulum
    #RAnkle_pitch = float(input("RAnkle_pitch: "))#-0.55
    RAnkle_pitch = -0.55
    RKnee_pitch = -0.016 * RAnkle_pitch**2 + 0.65
    RHip_pitch = -0.1*RAnkle_pitch #- 0.4

    LHip_pitch = 0.2 - RHip_pitch
    LKnee_pitch = 0.2
    # Solving the whole kinematic chain
    LAnkle_pitch = - LKnee_pitch - LHip_pitch - RAnkle_pitch - RHip_pitch - RKnee_pitch

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
    print("Lowering stepping leg")
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



    # 5- more inverted pendulum
    time.sleep(5)
    print("more back leg inverted pendelum")
    #RAnkle_pitch = float(input("RAnkle_pitch: "))#-0.65
    RAnkle_pitch = -0.68
    RKnee_pitch = -0.016 * RAnkle_pitch**2 + 0.65
    RHip_pitch = -0.1*RAnkle_pitch #- 0.4

    LHip_pitch = 0.2 - RHip_pitch
    LKnee_pitch = 0.2
    # Solving the whole kinematic chain
    LAnkle_pitch = - LKnee_pitch - LHip_pitch - RAnkle_pitch - RHip_pitch - RKnee_pitch

    if RAnkle_pitch == 0.0:
        RAnkle_pitch_pub.publish(-0.233)
    else:   
        RAnkle_pitch_pub.publish(RAnkle_pitch)
        RHip_pitch_pub.publish(RHip_pitch)
        RKnee_pitch_pub.publish(RKnee_pitch)

        LHip_pitch_pub.publish(LHip_pitch)
        LKnee_pitch_pub.publish(LKnee_pitch)
        LAnkle_pitch_pub.publish(LAnkle_pitch)


    #rospy.loginfo(f"\nLeft hip: {LHip_pitch}\t\t\t\tRighthip:{RHip_pitch}\nLeft ankle{LAnkle_pitch}\t\tRight ankle{RAnkle_pitch}")

    # Shifting the weight on top of the front leg
    time.sleep(4)
    print("Moving weight forward")
    LAnkle_roll = 0.17
    LHip_roll   = -LAnkle_roll
    RAnkle_roll = LAnkle_roll
    RHip_roll   = -RAnkle_roll

    shift = 0.17
    LAnkle_pitch = 0.32
    LKnee_pitch = -0.016 * LAnkle_pitch**2 - 0.65
    LHip_pitch  = LAnkle_pitch #+ 0.167

    RHip_pitch  = RHip_pitch   + shift
    RAnkle_pitch= RAnkle_pitch - shift


    LAnkle_roll_pub.publish(LAnkle_roll)
    LHip_roll_pub.publish(LHip_roll)
    RAnkle_roll_pub.publish(RAnkle_roll)
    RHip_roll_pub.publish(RHip_roll)

    LKnee_pitch_pub.publish(LKnee_pitch)

    LHip_pitch_pub.publish(LHip_pitch)
    RHip_pitch_pub.publish(RHip_pitch)
    LAnkle_pitch_pub.publish(LAnkle_pitch)
    RAnkle_pitch_pub.publish(RAnkle_pitch)





    # pushing the ground with front leg using
    # you guessed it INVERTED PENDELUM
    #LAnkle_pitch= float(input("LAnkle_pitch: "))
    time.sleep(5)
    LAnkle_pitch = 0.32
    LKnee_pitch = -0.016 * LAnkle_pitch**2 - 0.65
    LHip_pitch  = LAnkle_pitch #+ 0.167

    LAnkle_roll = 0.17
    LHip_roll   = 0.0
    RAnkle_roll = LAnkle_roll
    RHip_roll   = -RAnkle_roll 

    # Moving the back leg forward
    RHip_pitch = -0.5
    RKnee_pitch = 1.57
    RAnkle_pitch=-RKnee_pitch -RHip_pitch - LAnkle_pitch - LHip_pitch - LKnee_pitch

    if LAnkle_pitch == 0.0:
        LAnkle_pitch_pub.publish(0.233)
    else:
        LAnkle_roll_pub.publish(LAnkle_roll)
        LHip_roll_pub.publish(LHip_roll)
        RAnkle_roll_pub.publish(RAnkle_roll)
        RHip_roll_pub.publish(RHip_roll)

        time.sleep(3)
        print("Front leg inverted pendulum")
        LHip_pitch_pub.publish(LHip_pitch)
        LKnee_pitch_pub.publish(LKnee_pitch)
        LAnkle_pitch_pub.publish(LAnkle_pitch)
        # lifting the back leg
        RKnee_pitch_pub.publish(RKnee_pitch)
        RAnkle_pitch_pub.publish(RAnkle_pitch)
        #time.sleep(1)
        RHip_pitch_pub.publish(RHip_pitch)

        time.sleep(4)
        print("Resetting")
        neutralPosition('LR')





    



    
        


    


    
    

    print("------Done------\n")