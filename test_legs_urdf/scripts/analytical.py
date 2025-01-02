import rospkg
import rospy
from std_msgs.msg import Float64
import math
import numpy as np

# Initialize node
rospy.init_node('Nours_sad_publishing_node', anonymous=False)
rate = rospy.Rate(10)  # Frequency in Hz

# ROS Publishers
RAnkle_roll_pub = rospy.Publisher('/RAnkle_roll_position_controller/command', Float64, queue_size=5)
RAnkle_pitch_pub = rospy.Publisher('/RAnkle_pitch_position_controller/command', Float64, queue_size=5)
RKnee_pitch_pub = rospy.Publisher('/RKnee_pitch_position_controller/command', Float64, queue_size=5)
RHip_pitch_pub = rospy.Publisher('/RHip_pitch_position_controller/command', Float64, queue_size=5)
RHip_roll_pub = rospy.Publisher('/RHip_roll_position_controller/command', Float64, queue_size=5)
RHip_yaw_pub = rospy.Publisher('/RHip_yaw_position_controller/command', Float64, queue_size=5)

LAnkle_roll_pub = rospy.Publisher('/LAnkle_roll_position_controller/command', Float64, queue_size=5)
LAnkle_pitch_pub = rospy.Publisher('/LAnkle_pitch_position_controller/command', Float64, queue_size=5)
LKnee_pitch_pub = rospy.Publisher('/LKnee_pitch_position_controller/command', Float64, queue_size=5)
LHip_pitch_pub = rospy.Publisher('/LHip_pitch_position_controller/command', Float64, queue_size=5)
LHip_roll_pub = rospy.Publisher('/LHip_roll_position_controller/command', Float64, queue_size=5)
LHip_yaw_pub = rospy.Publisher('/LHip_yaw_position_controller/command', Float64, queue_size=5)

# Constants
g = 9.81  # Gravity (m/s^2)
z = 0.127   # Height (m)
l1 = 0.053  # Length of first link (m)
l2 = 0.079    # Length of second link (m)
v0 = 0.1  # Initial velocity (m/s)
v1 = 0.2  # Final velocity (m/s)
xs = 0    # Initial x-position (m)
s1 = 0.2  # Step size (m)

# Time constant and energy terms
Tc = z / g
E0 = (-g / (2 * z)) * (xs)**2
E1 = (1 / 2) * (v1)**2

# Support leg exchange position
xf0 = (z / (s1 * g)) * (E1 - E0) + s1 / 2

# Final time
a = Tc * math.asinh(xf0 / (Tc * v0))
A = (s1 - xf0) - Tc * np.sqrt(2*E1 + (g/z)*xf0**2)
B = 2*xf0
C = (s1 - xf0) + Tc * np.sqrt(2*E1 + (g/z)*xf0**2)
b = Tc * np.log((-B - np.sqrt(B**2 - 4*A*C)) / (2*A))


# Functions for kinematics
def x1(x):
    return xs * np.cosh(x / Tc) + Tc * v0 * np.sinh(x / Tc)

def x2(x):
    return (xf0-s1) * np.cosh((x-a)/ Tc) + Tc * ((2*E1+(g/z)*xf0**2)**(1/2)) * np.sinh((x-a)/ Tc)

def x3(x):
    return -1*x1(-1*(x-10))

def theta11(x):
    return np.arctan(x1(x) / z) * (180 / math.pi)

def theta12(x):
    theta1_val = theta11(x)  # Compute theta1
    arg = (l2**2 - (z / np.cos(np.radians(theta1_val)))**2 - l1**2) / (2 * (z / np.cos(np.radians(theta1_val))) * l1)
    arg = np.clip(arg, -1, 1)  # Ensure arg is within [-1, 1] to avoid NaN
    return 180 - np.degrees(np.arccos(arg))

def theta13(x):
    theta2_val = theta12(x)  # Compute theta2
    return np.degrees(np.arcsin((-l2 / l1) * np.sin(np.radians(theta2_val))))

# Time range for motion
t_values = np.linspace(0, a, 50)

while not rospy.is_shutdown():

    Step = float(input("Enter Step: "))

    # Initial positions for standing
    if Step == 0.0:
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
    
        LAnkle_pitch_pub.publish(LAnkle_pitch)
        LKnee_pitch_pub.publish(LKnee_pitch)
        LHip_pitch_pub.publish(LHip_pitch)
        LHip_roll_pub.publish(LHip_roll)
        RHip_roll_pub.publish(RHip_roll)
        RAnkle_roll_pub.publish(RAnkle_roll)
        LAnkle_roll_pub.publish(LAnkle_roll)
        RHip_pitch_pub.publish(RHip_pitch)
        RKnee_pitch_pub.publish(RKnee_pitch)
        RAnkle_pitch_pub.publish(RAnkle_pitch)       
        
    if Step > 0.0:

        #first step is to shift weight to one leg
        LAnkle_roll = 0.15 #rad
        RAnkle_roll = LAnkle_roll

        RHip_roll   = -RAnkle_roll
        LHip_roll   = -LAnkle_roll

        LAnkle_roll_pub.publish(LAnkle_roll)
        LHip_roll_pub.publish(LHip_roll)
        RAnkle_roll_pub.publish(RAnkle_roll)
        RHip_roll_pub.publish(RHip_roll)

        #second step is to lift the leg that isnt holding the weight
        RAnkle_pitch = 0.4 #rad
        RKnee_pitch = -0.016 * RAnkle_pitch**2 + 0.65
        RHip_pitch  = -3*RAnkle_pitch + 0.4

        RHip_pitch_pub.publish(RHip_pitch)
        RKnee_pitch_pub.publish(RKnee_pitch)
        RAnkle_pitch_pub.publish(RAnkle_pitch)


        #first step is to shift weight to one leg
        LAnkle_roll = -0.5 #rad
        RAnkle_roll = LAnkle_roll

        RHip_roll   = -RAnkle_roll
        LHip_roll   = -LAnkle_roll

        LAnkle_roll_pub.publish(LAnkle_roll)
        LHip_roll_pub.publish(LHip_roll)
        RAnkle_roll_pub.publish(RAnkle_roll)
        RHip_roll_pub.publish(RHip_roll)

        #  Publishing loop
        for t_val in t_values[:int(len(t_values)/2)]:
            try:
                # Compute angles
                theta2_val = theta12(t_val)
                theta3_val = theta13(t_val)

                # Right leg kinematics
                LAnkle_pitch_pub.publish(Float64(theta2_val))
                LKnee_pitch_pub.publish(Float64(theta3_val))

                # Log the values
                rospy.loginfo(f"Published: RAnkle_pitch = {theta2_val}, RKnee_pitch = {theta3_val}")

                # Sleep to maintain publishing rate
                rate.sleep()
            except Exception as e:
                rospy.logerr(f"Error during computation or publishing: {e}")
                break