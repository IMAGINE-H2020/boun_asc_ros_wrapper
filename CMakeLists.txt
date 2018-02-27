cmake_minimum_required(VERSION 2.8.3)
project(asc)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  std_msgs
  message_generation
  cv_bridge
)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  NodeInfo.msg
  NodeList.msg
)



## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs
 )

 install(
   DIRECTORY scripts/
   DIRECTORY scripts/AffordanceNodes
   DIRECTORY scripts/AftionEffectNodes
   DIRECTORY scripts/PerceptionNodes
   DIRECTORY scripts/SceneDescriptorNodes
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   USE_SOURCE_PERMISSIONS
 )

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES asc
  CATKIN_DEPENDS roscpp rospy sensor_msgs std_msgs message_runtime
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
