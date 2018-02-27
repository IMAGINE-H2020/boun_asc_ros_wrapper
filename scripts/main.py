#!/usr/bin/env python
import sys
import rospy
import rospkg

from TopicWrapper import TopicWrapper


if __name__ == "__main__":
    rospy.init_node('ASC')
    rate = rospy.Rate(20)
    perceptionWrapper = TopicWrapper('Perception')
    sceneDescriptorWrapper = TopicWrapper('SceneDescriptor')
    actionEffectWrapper = TopicWrapper('ActionEffect')
    affordanceWrapper = TopicWrapper('Affordances')
    while not rospy.is_shutdown():
        perceptionWrapper.publishList()
        sceneDescriptorWrapper.publishList()
        actionEffectWrapper.publishList()
        affordanceWrapper.publishList()
        rate.sleep()
