import rospkg
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float32
from control_msgs.msg import JointControllerState
from sensor_msgs.msg import JointState
import time
import math

#ros topics

# Publisher_name = rospy.Publisher('topic_name', msg_type, queue_size=5)

# Angles publishers
RAnkle_roll_pub = rospy.Publisher('rankle_roll_servo_angle', Float32, queue_size=5)
RAnkle_pitch_pub= rospy.Publisher('rankle_pitch_servo_angle', Float32, queue_size=5)
RKnee_pitch_pub = rospy.Publisher('rknee_pitch_servo_angle', Float32, queue_size=5)
RHip_pitch_pub  = rospy.Publisher('rhip_pitch_servo_angle', Float32, queue_size=5)
RHip_roll_pub   = rospy.Publisher('rhip_roll_servo_angle', Float32, queue_size=5)
#RHip_yaw_pub    = rospy.Publisher('/lhip_yaw_position_controller/command', Float32, queue_size=5)

LAnkle_roll_pub = rospy.Publisher('lankle_roll_servo_angle', Float32, queue_size=5)
LAnkle_pitch_pub= rospy.Publisher('lankle_pitch_servo_angle', Float32, queue_size=5)
LKnee_pitch_pub = rospy.Publisher('lknee_pitch_servo_angle', Float32, queue_size=5)
LHip_pitch_pub  = rospy.Publisher('lhip_pitch_servo_angle', Float32, queue_size=5)
LHip_roll_pub   = rospy.Publisher('lhip_roll_servo_angle', Float32, queue_size=5)
#LHip_yaw_pub    = rospy.Publisher('/lhip_yaw_position_controller/command', Float32, queue_size=5)


# Subscriber callbacks
# name: 
#0   - LAnkle_pitch
#1   - LAnkle_roll
#2   - LHip_pitch
#3   - LHip_roll
#4   - LHip_yaw
#5   - LKnee_pitch
#6   - RAnkle_pitch
#7   - RAnkle_roll
#8   - RHip_pitch
#9   - RHip_roll
#10  - RHip_yaw
#11  - RKnee_pitch

def callback(data):
    print("-----------------------------------------------\n", data.name[9],data.position[9])
    RAnkle_roll_pub.publish(rad2servo(data.position[7]))
    RAnkle_pitch_pub.publish(rad2servo(-data.position[6]))
    RKnee_pitch_pub.publish(rad2servo(data.position[11]))
    RHip_pitch_pub.publish(rad2servo(data.position[8]))
    RHip_roll_pub.publish(rad2servo(data.position[9]))

    LAnkle_roll_pub.publish(rad2servo(data.position[1]))
    LAnkle_pitch_pub.publish(rad2servo(-data.position[0]))
    LKnee_pitch_pub.publish(rad2servo(data.position[5]))
    LHip_pitch_pub.publish(rad2servo(data.position[2]))
    LHip_roll_pub.publish(rad2servo(data.position[3]+0.15))



#defining node
rospy.init_node('Nours_translator_node', anonymous=False)
rate = rospy.Rate(10) # Hz 


# subscribers
rospy.Subscriber("/joint_states", JointState, callback)




def rad2servo(rad):
    return rad*(90/1.57)+90





while not rospy.is_shutdown():

    rospy.spin()

    

    

    print("------Done------\n")