#!/usr/bin/env python
from homework_two.srv import *
import rospy
def handle_add_two_ints(req):
    server_time = rospy.get_time()
    return float64(server_time)
def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print "Ready to add two ints."
    rospy.spin()
if __name__ == "__main__":
    add_two_ints_server()
