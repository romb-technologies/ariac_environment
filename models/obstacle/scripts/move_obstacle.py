#!/usr/bin/env python

import sys
import rospy
import numpy as np
from gazebo_msgs.msg import ModelState

def move_obstacle(start_position_x, end_position_x, start_position_y, end_position_y, increment):
    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
    rospy.init_node('move_node', anonymous=True)
    rate = rospy.Rate(10)


    start_x = start_position_x
    start_y = start_position_y 
    end_x = end_position_x
    end_y = end_position_y 

    pose_x = start_position_x
    pose_y = start_position_y


    if np.abs(end_x - start_x) > np.abs(end_y - start_y):
        inc_x = np.sign(end_x - start_x) * np.abs(increment)
        inc_y = float(np.abs(end_y - start_y))/np.abs(end_x - start_x) * np.abs(increment)
        inc_y = np.sign(end_y - start_y) * inc_y
    else:
        inc_y = np.sign(end_y - start_y) * np.abs(increment)
        inc_x = float(np.abs(end_x - start_x))/np.abs(end_y - start_y) * np.abs(increment)
        inc_x = np.sign(end_x - start_x) * inc_x


    temp_start_x = np.minimum(start_x, end_x)
    end_x = np.maximum(start_x, end_x)
    start_x = temp_start_x
    temp_start_y = np.minimum(start_y, end_y)
    end_y = np.maximum(start_y, end_y)
    start_y = temp_start_y

    msg = ModelState()
    msg.model_name = 'obstacle'
    msg.pose.position.x = pose_x
    msg.pose.position.y = pose_y
    msg.pose.position.z = 1.25

    while not rospy.is_shutdown():
        if (inc_x > 0 and pose_x > end_x) or (inc_x < 0 and pose_x < start_x) or \
        (inc_y > 0 and pose_y > end_y) or (inc_y < 0 and pose_y < start_y):
            inc_x = -inc_x
            inc_y = -inc_y
        pose_x = pose_x + inc_x
        pose_y = pose_y + inc_y
        msg.pose.position.x = pose_x
        msg.pose.position.y = pose_y
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        start_x = float(sys.argv[1])
        end_x = float(sys.argv[2])
        start_y = float(sys.argv[3])
        end_y = float(sys.argv[4])
        increment = float(sys.argv[5])
        move_obstacle(start_x, end_x, start_y, end_y, increment)
    except rospy.ROSInterruptException:
        pass