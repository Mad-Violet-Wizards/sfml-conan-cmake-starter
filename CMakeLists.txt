cmake_minimum_required(VERSION 3.15)

project(sfml-conan-cmake-starter)

set(CMAKE_CXX_STANDARD 20)

add_library(LIBS include/Basic.hpp src/Basic.cpp)

# Include Conan.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} src/main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE LIBS)