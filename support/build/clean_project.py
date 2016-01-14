# -*- c-file-style: "sourcery" -*-
#
# Use and distribution of this software and its source code is governed
# by the terms and conditions defined in the "LICENSE" file that is part
# of this source code package.
#
"""
Remove build artifacts not normally managed by the default "clean" phase
"""
import os
import glob
import shutil

from pybuilder.core  import use_plugin
from pybuilder.core  import init
from pybuilder.core  import task
from pybuilder.core  import depends
from pybuilder.core  import description
from pybuilder.utils import apply_on_files

use_plugin("core")


@init
def init_clean_project_plugin(project) :
    project.set_property_if_unset("clean_project_files_glob", [])


@task
@depends("clean")
@description("Cleans build artifacts from project directories.")
def clean_project(project, logger) :
    file_globs = project.get_mandatory_property("clean_project_files_glob")
    if not file_globs :
        logger.warn("No files to clean configured. Consider removing plugin.")
        return

    for file_glob in file_globs :
        clean_project_files(file_glob, logger)


def clean_project_files(path_or_glob, logger) :
    """
    Resolve file name references and ensure they are properly deleted
    """
    if "*" in path_or_glob :
        files_to_clean = glob.glob(path_or_glob)
    else :
        files_to_clean = [os.path.expanduser(path_or_glob)]

    for file_to_clean in files_to_clean :
        if not os.path.exists(file_to_clean) :
            continue

        if os.path.isdir(file_to_clean) :
            logger.info("Removing directory {}".format(file_to_clean))
            shutil.rmtree(file_to_clean)
        else :
            logger.info("Removing file {}".format(file_to_clean))
            os.remove(file_to_clean)
