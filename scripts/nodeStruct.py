#!/usr/bin/env python


"""
    Node class for holding rosmessage related to nodeInfo.msg

"""
class nodeStruct:
    def __init__(self,nodeId,purposeId,nodeTopic,description):
        self.nodeId=nodeId
        self.purposeId=purposeId
        self.nodeTopic=nodeTopic
        self.description=description
