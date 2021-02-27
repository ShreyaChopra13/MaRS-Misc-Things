#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32

def sub_func():
	rospy.init_node("reciever")
	rospy.Subscriber("/pipe1", Int32, hearing_func)
	rospy.spin()

def hearing_func(msg):
    rospy.loginfo("data recieved from terminal = %u",msg.data)

if __name__=='__main__':
	sub_func()	
