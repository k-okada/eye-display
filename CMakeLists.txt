cmake_minimum_required(VERSION 3.0.2)
project(eye_display)

find_package(catkin REQUIRED COMPONENTS message_generation)

catkin_python_setup()

add_message_files(FILES
  KeyValue.msg
  KeyValueArray.msg
#  DIRECTORY rosserial_ex/msg  # this message should be remove once rosserial_client is updated
)

add_service_files(FILES
  RequestParam.srv
#  DIRECTORY rosserial_ex/srv
)

generate_messages()

catkin_package(CATKIN_DEPENDS message_runtime)

include_directories()

catkin_install_python(PROGRAMS
  node_scripts/build.py node_scripts/demo_move_eye.py node_scripts/pub_eye_status.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/node_scripts)

# this programs should be remove once rosserial_client is updated
catkin_install_python(PROGRAMS
  rosserial_ex/serial_node.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/node_scripts)
