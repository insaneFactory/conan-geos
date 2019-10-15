cmake_minimum_required(VERSION 3.1.2)
project(Conan-GEOS)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_subdirectory(source_subfolder)