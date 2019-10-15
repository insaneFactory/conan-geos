from conans import ConanFile, CMake, tools
import os


class GeosConan(ConanFile):
    name = "geos"
    version = "3.8.0"
    license = "LGPL-2.1"
    url = "https://trac.osgeo.org/geos"
    description = "GEOS (Geometry Engine - Open Source) is a C++ port of the ​JTS Topology Suite (JTS). It aims to contain the complete functionality of JTS in C++. This includes all the ​OpenGIS Simple Features for SQL spatial predicate functions and spatial operators, as well as specific JTS enhanced functions."
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
	    "fPIC": [True, False]
    }
    default_options = {
        "shared": True,
        "fPIC": True
    }
    #generators = "cmake"
    _source_subfolder = "source_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        archive_name = "geos-%s" % self.version
        tools.get("http://download.osgeo.org/geos/%s.tar.bz2" % archive_name)
        os.rename(archive_name, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["GEOS_ENABLE_TESTS"] = False
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["geos", "geos_c"]

