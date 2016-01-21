#!/usr/bin/env python
#
# Main entry point for package setup
#
import io
import os
import re

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup
from setuptools import Command

#
# Function to read a file. Used for populating setup.py configuration
# options.
#
def read(*args, **kwargs) :
    return io.open(join(dirname(__file__), *args), encoding=kwargs.get("encoding", "utf8")).read()


#
# Custom clean command specified as a setup cmdclass extension.
#
class RealClean(Command) :
    """Custom clean command to tidy up the project root."""

    user_options = []

    def initialize_options(self) :
        pass

    def finalize_options(self) :
        pass

    def run(self) :
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info ./src/*.egg-info')




kwargs = {
    "name"                 : "change-detect",
    "version"              : "0.1.0",
    "license"              : "MPL",
    "description"          : "Covariate shift detector.",
    "long_description"     : "{0}\n".format(read("README.rst")),
    "author"               : "Paolo de Dios",
    "author_email"         : "paolodedios@gmail.com",
    "url"                  : "http://appliedtheory.io/",
    "packages"             : find_packages("src"),
    "package_dir"          : {"" : "src"},
    "py_modules"           : [splitext(basename(path))[0] for path in glob("src/*.py")],
    "include_package_data" : True,
    "zip_safe"             : False,
    "classifiers"          : [
        # For a complete classifier list, @see http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
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
        "Topic :: Utilities",
    ],
    "keywords"             : [
        # eg: "keyword1", "keyword2", "keyword3",
    ],
    "install_requires"     : [
        # eg: "aspectlib==1.1.1", "six>=1.7",
    ],
    "extras_require"       : {
        # eg: "rst": ["docutils>=0.11"],
    },
    "entry_points"         : {
        "console_scripts": [
            "shift_detect = shift_detect.__main__:main"
        ]
    },
    "cmdclass"             : {
        "realclean" : RealClean
    },
}

setup(**kwargs)
