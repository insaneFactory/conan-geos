################################################################################
# Part of CMake configuration for GEOS
#
# Copyright (C) 2018 Mateusz Loskot <mateusz@loskot.net>
#
# This is free software; you can redistribute and/or modify it under
# the terms of the GNU Lesser General Public Licence as published
# by the Free Software Foundation.
# See the COPYING file for more information.
################################################################################

add_executable(test_big_sweep_line_speed
    TestSweepLineSpeed.cpp
    GeometryTestFactory.cpp)
target_link_libraries(test_big_sweep_line_speed PRIVATE CONAN_PKG::geos)
