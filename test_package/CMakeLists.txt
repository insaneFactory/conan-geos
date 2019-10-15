cmake_minimum_required(VERSION 3.1.2)
project(PackageTest-GEOS CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_subdirectory(tests)