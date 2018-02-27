#!/usr/bin/env python

import numpy as np
import rospy
import rospkg

import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from asc.msg import *

if __name__ == "__main__":
    rospy.init_node('DummyLeverUpPositionDetector')
    rate = rospy.Rate(100)
    lever_up_mask = cv2.imread('lever_up_mask.png')

    lever_up_pub = rospy.Publisher("lever_up_locations",Image,queue_size=1)
    asc_pub = rospy.Publisher("/SceneDescriptorNewNodeListener",NodeInfo,queue_size=1)
    bridge = CvBridge()
    imageMsg=bridge.cv2_to_imgmsg(lever_up_mask, "bgr8")

    lever_up_node=NodeInfo()
    lever_up_node.nodeId='DummyLeverUp'
    lever_up_node.purposeId='Lever_Up_Mask'
    lever_up_node.nodeTopic='lever_up_locations'
    lever_up_node.description='This is simple scene descriptor that shows where' \
    ' PCB is lever uppable, normally this was done in MATLAB.Currenly since code'\
    ' is not integrated it reads an image and send it as ros message'

    for i in range(20): ## Currently, this topic is not rosservice, so this kind of hack is necessary.
        asc_pub.publish(lever_up_node)
        rate.sleep()

    rate.sleep()
    while not rospy.is_shutdown():
        lever_up_pub.publish(imageMsg)

        rate.sleep()
