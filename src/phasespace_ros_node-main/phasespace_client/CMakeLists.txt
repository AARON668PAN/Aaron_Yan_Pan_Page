cmake_minimum_required(VERSION 3.5)
project(phasespace_client)


if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()


find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(phasespace_msgs REQUIRED)


include_directories(
  include
)


link_directories(
  bin
)

add_library(owlsock SHARED IMPORTED)
set_target_properties(owlsock PROPERTIES IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/bin/libowlsock.so)

add_library(${PROJECT_NAME} src/psnode.cpp)
ament_target_dependencies(${PROJECT_NAME} rclcpp phasespace_msgs)

add_executable(${PROJECT_NAME}_node src/psnode.cpp)
target_link_libraries(${PROJECT_NAME}_node owlsock ${PROJECT_NAME})

add_executable(listener src/listener.cpp)
ament_target_dependencies(listener rclcpp std_msgs phasespace_msgs)
install(TARGETS listener
  DESTINATION lib/${PROJECT_NAME})

install(TARGETS
  ${PROJECT_NAME}_node
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

