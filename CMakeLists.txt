cmake_minimum_required(VERSION 3.20.0)
set(CXX_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS, "${CXX_FLAGS}")

add_definitions(-std=c++11)

project(TheUltimateSup)

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )


add_executable(${PROJECT_NAME} main.cpp Adder/adder.cpp)

target_link_libraries( ${PROJECT_NAME} ${OpenCV_LIBS} )



