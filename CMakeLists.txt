cmake_minimum_required(VERSION 2.8.3)
project(throttle_debug)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  sensor_msgs
  std_msgs
)

add_message_files(
  FILES
  TwoArrayWithHeader.msg
  TwoArrayWithoutHeader.msg
  OneArrayWithHeader.msg
  OneArrayWithoutHeader.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
)

catkin_package(
)
