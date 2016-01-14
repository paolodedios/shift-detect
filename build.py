# -*- c-file-style: "sourcery" -*-
#
# Use and distribution of this software and its source code is governed
# by the terms and conditions defined in the "LICENSE" file that is part
# of this source code package.
#
from pybuilder.core  import use_bldsup
from pybuilder.core  import use_plugin
from pybuilder.core  import init
from pybuilder.core  import task
from pybuilder.core  import Author
from pybuilder.utils import assert_can_execute

import glob
import os
import shutil

use_plugin("python.core")
use_plugin("python.flake8")
use_plugin("python.unittest")
use_plugin("python.integrationtest")
use_plugin("python.install_dependencies")

# Import local build support plugins
use_bldsup(build_support_dir="support/build")
use_plugin("copy_files")
use_plugin("clean_project")
use_plugin("distribute")
use_plugin("devpi")

# Declare default build phase tasks to execute
default_task = [ "clean_project", "analyze", "publish" ]

# Declare top level project properties
authors = [Author("Paolo de Dios", "paolodedios@gmail.com")]
name    = "change-detect"
url     = "http://paolodedios.com"
summary = "Covariate shift detector."
version = "0.1.0"
license = "ATCSL"


@init
def set_properties(project) :

    # Declare project build dependencies
    project.build_depends_on("mockito", ">=0.5.2")

    # Declare project runtime dependencies
    project.depends_on("six", ">=1.9")
    project.depends_on("docopt", ">=0.6.2")

    # Always upgrade runtime dependencies given the pinned version specs below
    project.set_property("install_dependencies_upgrade", True)

    # Declare the location of all unit tests
    project.set_property("dir_source_unittest_python", "src/test/unit/python")
    project.set_property("unittest_module_glob", "*_tests")
    project.set_property("unittest_test_method_prefix", "test")

    # Declare the location of all integration tests
    project.set_property("dir_source_integrationtest_python", "src/test/integration/python")
    project.set_property("integrationtest_module_glob", "*_tests")
    project.set_property("integrationtest_test_method_prefix", "test")

    # Disable Teamcity output during normal builds. When the TEAMCITY_VERSION
    # environment variable is set (by either Teamcity or a user), teamcity
    # output will be generated automatically
    project.set_property("teamcity_output", False)

    # Specify unit and integration test artifacts that can be removed with the
    # "clean_project" task
    project.get_property("clean_project_files_glob").extend([
        "{}/__pycache__".format(project.get_property("dir_source_unittest_python")),
        "{}/*.pyc".format(project.get_property("dir_source_unittest_python")),
        "{}/__pycache__".format(project.get_property("dir_source_integrationtest_python")),
        "{}/*.pyc".format(project.get_property("dir_source_integrationtest_python"))
        ])

    # Check sources during the analyze phase, but ignore certain PEP8 error codes.
    # @see http://pep8.readthedocs.org/en/latest/intro.html#error-codes
    project.set_property("flake8_ignore", "E201,E202,E203,E221,E272,E302,E303,E501")
    project.set_property("flake8_verbose_output", True)
    project.set_property("flake8_include_test_sources", True)
    project.set_property("flake8_break_build", False)

    # Copy files to the top level of the distribution staging directory
    project.set_property("copy_root_files_target", "$dir_dist")
    project.get_property("copy_root_files_glob").extend([
        "LICENSE",
        "README.rst",
        "support/dist/setup.cfg",
        "support/dist/tox.ini"
        ])

    # Declare which copied resources will be packaged for installation via
    # MAINIFEST.in
    project.install_file(".", "LICENSE")
    project.install_file(".", "README.rst")
    project.install_file(".", "tox.ini")

    # Package all scripts in the bin directory
    project.set_property("dir_dist_scripts", "bin")

    # Add PyPi package metdata data classifiers.
    #
    # Note: Invoking "setup.py release" will typically release all code to the
    # wild. In order to ensure that this doesn't accidentally happen during the
    # publish phase of the build, the "Private" classifier property is specified
    # by default. As a result the public PyPI service will reject this package
    # but a private PyPi or DevPI server will accept it.
    #
    # For a complete classifier list, @see http://pypi.python.org/pypi?%3Aaction=list_classifiers
    project.set_property("distutils_classifiers", [
        "Private :: Do Not Upload",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License"
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities"
        ])

    # Force setup.py to generate and install a shell script for the entry point
    project.set_property("distutils_console_scripts", [
        "change_detect = change_detect.__main__:main"
        ])

    # Extend the list of setup.py commands to be executed from sdist, bdist_dumb
    project.get_property("distutils_commands").extend([ "bdist_egg", "bdist_wheel" ])

    # Set user name and destination index for local devpi/PyPi central
    # repository
    project.set_property("devpi_user", "appliedtheory")
    project.set_property("devpi_developer_index", "dev")
    project.set_property("devpi_staging_index"  , "staging")
    project.set_property("devpi_release_index"  , "release")
