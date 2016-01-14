#!/usr/bin/env python
# -*- c-file-style: "sourcery" -*-
#
# Use and distribution of this software and its source code is governed
# by the terms and conditions defined in the "LICENSE" file that is part
# of this source code package.
#
"""
Initialization code for the "change_detect" package

For more information, read: https://docs.python.org/2/tutorial/modules.html
"""
from __future__ import print_function

import sys

__python_version__ = (2, 7)
__app_name__       = "Change Detector"
__log_module__     = "change_detect"
__version__        = "0.1.0"

if sys.version_info[:2] < __python_version__ :
    print("Change Detector requires Python version {}".format(".".join(map(str, __python_version__))), file=sys.stderr)
    sys.exit(1)
