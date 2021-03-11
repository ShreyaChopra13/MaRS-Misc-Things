#!/usr/bin/env python


import rospy
from std_msgs.msg import String


def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10) 
	while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()
   

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
 
    
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
#	listener()

