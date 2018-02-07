#!/usr/bin/env python
import rospy
import time
import numpy as np
import matplotlib.pyplot as plt
from homework_two.srv import *


def add_two_ints_client(x, y):
    rospy.init_node('add_two_ints',anonymous=True)
    rospy.wait_for_service('add_two_ints')
    add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
    resp1 = add_two_ints(x, y)

    return resp1.sum
    #rospy.spin()



if __name__ == "__main__":
    d=[]
    count = 800
    while(count>0):
        count = count - 1
        x = 1
        y = 1
        c_time = time.time()
        server_time = add_two_ints_client(x,y)
        diff = c_time-server_time
        d.append(diff*0.002)
        print server_time
    plt.hist(d,bins='auto',range=(0,0.005))
    plt.show()
