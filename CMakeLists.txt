cmake_minimum_required(VERSION 2.8.3)
project(package_name)
# add required packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  gazebo_ros
  control_msgs
  geometry_msgs
  message_generation
)

# message files if you want to create custom messages
add_message_files(
  FILES
  PackageMsg.msg # update with your message file name in msg folder
)

# service files if you want to create custom services
add_service_files(
  FILES
  PackageSrv.srv # update with your service file name in srv folder
)

# setup the package - it will run setup.py
catkin_python_setup()

# generate added messages and services
generate_messages(
  DEPENDENCIES
  std_msgs
)

# add catkin dependencies
catkin_package(
  CATKIN_DEPENDS message_runtime
  rospy
  std_msgs
)

# install python scripts
catkin_install_python(PROGRAMS 
    scripts/node # add nodes here 
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)