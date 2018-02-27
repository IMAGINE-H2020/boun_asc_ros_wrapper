#!/usr/bin/env python

import numpy as np
import rospy
import rospkg

import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from asc.msg import *

if __name__ == "__main__":
    rospy.init_node('DummyPerception')
    rate = rospy.Rate(100)
    pcb = cv2.imread('pcb.png')
    pcb_processed = cv2.imread('pcb_blob.png')

    image_pub = rospy.Publisher("camera",Image,queue_size=1)
    image_pub2 = rospy.Publisher("pcb_processed",Image,queue_size=1)
    asc_pub = rospy.Publisher("/PerceptionNewNodeListener",NodeInfo,queue_size=1)
    bridge = CvBridge()
    imageMsg=bridge.cv2_to_imgmsg(pcb, "bgr8")
    imageMsg2=bridge.cv2_to_imgmsg(pcb_processed, "bgr8")

    cameraNodeInfo=NodeInfo()
    cameraNodeInfo.nodeId='DummyCamera'
    cameraNodeInfo.purposeId='Camera'
    cameraNodeInfo.nodeTopic='camera'
    cameraNodeInfo.description='This is simple dummy camera simulation that reads an image and send it as ros message'

    blobNodeInfo=NodeInfo()
    blobNodeInfo.nodeId='Dummy_Pcb_blob'
    blobNodeInfo.purposeId='Pcb_Blob'
    blobNodeInfo.nodeTopic='pcb_processed'
    blobNodeInfo.description='This is simple dummy model that supposedly find pcb blob, publish it. Currently it reads an image and send it as ros message'

    for i in range(20): ## Currently, this topic is not rosservice, so this kind of hack is necessary.
        asc_pub.publish(blobNodeInfo)
        rate.sleep()
        asc_pub.publish(cameraNodeInfo)
        rate.sleep()

    rate.sleep()
    while not rospy.is_shutdown():
        image_pub.publish(imageMsg)
        image_pub2.publish(imageMsg2)

        rate.sleep()
