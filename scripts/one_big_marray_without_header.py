#!/usr/bin/env python
import rospy
from std_msgs.msg import *


rospy.init_node("one_big_marray_without_header")
pub = rospy.Publisher("/hoge", Float32MultiArray, queue_size=1)
rate = rospy.Rate(120)

while(not rospy.is_shutdown()):
    pub.publish(Float32MultiArray(data=[0.]*1000))
    rate.sleep()

