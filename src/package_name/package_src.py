#!/usr/bin/env python
import rospy
import roslib

# import message and service types
from package_name.msg import PackageMsg
from package_name.srv import PackageSrv
from std_msgs.msg import String

class PackageClass(object):
    def __init__(self, id):
        self.id = id
        # define service client
        self.service_client = rospy.ServiceProxy('package_name/service', PackageSrv, self.service_callback)
        # subscribe to topic
        self.subscriber = rospy.Subscriber('/topic', String, self._callback)

    def service_callback(self, request):
        # define service callback
        response = self.id
        return response
    
    def _callback(self, msg):
        # define topic callback
        pass