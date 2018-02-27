#!/usr/bin/env python

import rospy
import rospkg
from asc.msg import *
from nodeStruct import nodeStruct
class TopicWrapper:
    def __init__(self,wrapperType):
        self.nodeList=list()
        self.nodeIdList=list()
        self.nodeTopicList=list()
        #self.purposeDict=dict() TODO:Add this
        self.wrapperType=wrapperType
        self.pub=rospy.Publisher(wrapperType+'NodeLister', NodeList, queue_size=1)
        self.sub=rospy.Subscriber(wrapperType+'NewNodeListener', NodeInfo, self.addNewNodeCallback) ## TODO: Need to be converted to ros service

    def publishList(self):
        nodeList=NodeList()
        nodeList.header=rospy.Header()
        nodeList.nodeList=list()
        for i in range(len(self.nodeList)):
            node=NodeInfo()
            node.nodeId=self.nodeList[i].nodeId
            node.purposeId=self.nodeList[i].purposeId
            node.nodeTopic=self.nodeList[i].nodeTopic
            node.description=self.nodeList[i].description
            nodeList.nodeList.append(node)
        self.pub.publish(nodeList)
    def addNewNodeCallback(self,data):
        print ('here')
        newNode=nodeStruct(data.nodeId,data.purposeId,data.nodeTopic,data.description)
        if data.nodeId in self.nodeIdList:
            print("This topic is already added to " +self.wrapperType+  " Nodes")
            return;
        if data.nodeTopic in self.nodeTopicList:
            print("This topic already added to " +self.wrapperType+  " Nodes")
            return;
        self.nodeIdList.append(data.nodeId)
        self.nodeTopicList.append(data.nodeTopic)
        self.nodeList.append(newNode)
        print('New Node Added Succesfully')
