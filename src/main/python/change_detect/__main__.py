#!/usr/bin/env python
# -*- c-file-style: "sourcery" -*-
#
# Use and distribution of this software and its source code is governed
# by the terms and conditions defined in the "LICENSE" file that is part
# of this source code package.
#
"""
Main entry point when running the "change_detect" package

For more information, read:
  https://www.python.org/dev/peps/pep-0338/
  https://docs.python.org/2/using/cmdline.html#cmdoption-m
  https://docs.python.org/3/using/cmdline.html#cmdoption-m

If this package depends on functions and variables defined in __init__.py, then
this package should be instead executed with:
  $ python -m change_detect
"""
from __future__ import print_function

import sys

def main(argv=()) :
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: Program exit status code
    """

    print(argv, file=sys.stdout)

    return 0


if __name__ == "__main__" :
    sys.exit(main())
