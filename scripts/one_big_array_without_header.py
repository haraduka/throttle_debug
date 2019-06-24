#!/usr/bin/env python
import rospy
from throttle_debug.msg import *


rospy.init_node("one_big_array_without_header")
pub = rospy.Publisher("/hoge", OneArrayWithoutHeader, queue_size=10)
rate = rospy.Rate(125)

while(not rospy.is_shutdown()):
    pub.publish(OneArrayWithoutHeader(array1=[0.]*1000))
    rate.sleep()

