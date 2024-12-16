import rospkg
import rospy
from std_msgs.msg import Float64

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





#angles msgs in rad
#These numbers are for standing up and ready to move
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



#defining node
rospy.init_node('Nours_sad_publishing_node', anonymous=False)
rate = rospy.Rate(10) # Hz 


#sending data
LHip_yaw_pub.publish(LHip_yaw)