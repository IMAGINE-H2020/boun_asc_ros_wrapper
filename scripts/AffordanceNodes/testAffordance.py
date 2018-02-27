#!/usr/bin/env python

import numpy as np
import rospy
import rospkg

import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import String
from asc.msg import *

lever_up_location_sub =None
lever_up_image=None
affordanceList=dict()
bridge = CvBridge()
def imageCallback(data):
    try:
        lever_up_image = bridge.imgmsg_to_cv2(data, "mono8")
    except CvBridgeError as e:
        print(e)
    global affordanceList
    count0=0
    count1=0
    if(np.sum(np.sum(lever_up_image))):
        affordanceList['Lever_Uppable']=1
    else:
        my_dict.pop('Lever_Uppable', None)



def connectSc(data):
    global lever_up_location_pub
    possibleLeverUpMasks=list()
    for node in data.nodeList:
        if(node.purposeId=='Lever_Up_Mask'):
            possibleLeverUpMasks.append(node)
    lever_up_location_sub=rospy.Subscriber(possibleLeverUpMasks[0].nodeTopic,Image,imageCallback)



if __name__ == "__main__":
    rospy.init_node('DummyAffordanceDetector')
    rate = rospy.Rate(100)
    affordance_pub = rospy.Publisher("Affordances",String,queue_size=1)
    asc_pub = rospy.Publisher("/AffordancesNewNodeListener",NodeInfo,queue_size=1)
    asc_sub = rospy.Subscriber("/SceneDescriptorNodeLister",NodeList,connectSc)

    #
    #imageMsg=bridge.cv2_to_imgmsg(lever_up_mask, "bgr8")

    affordance_node=NodeInfo()
    affordance_node.nodeId='DummyAffordance'
    affordance_node.purposeId='Affordance_Detector'
    affordance_node.nodeTopic='Affordances'
    affordance_node.description='This is a simple affordance detector. It tells actions that are affordable.'\
    'Currently, this model doesn\'t consider tools, action descriptor and many important constraint.' \
    'This model is just for showcasing ASC'

    for i in range(20): ## Currently, this topic is not rosservice, so this kind of hack is necessary.
        asc_pub.publish(affordance_node)
        rate.sleep()

    rate.sleep()
    Affordances=String()
    Affordances.data=''
    for key in affordanceList.keys():
        Affordances.data=Affordances.data+' '+key
    while not rospy.is_shutdown():
        affordance_pub.publish(Affordances)
        rate.sleep()
