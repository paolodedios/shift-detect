# -*- c-file-style: "sourcery" -*-
#
# Use and distribution of this software and its source code is governed
# by the terms and conditions defined in the "LICENSE" file that is part
# of this source code package.
#
"""
Copies files specified in the copy_files_glob list to the top level
of the copy_files_target
"""
import os
import shutil

from pybuilder.core  import use_plugin
from pybuilder.core  import init
from pybuilder.core  import task
from pybuilder.utils import apply_on_files

use_plugin("core")


@init
def init_copy_files_plugin(project) :
    project.set_property_if_unset("copy_root_files_target", "$dir_target")
    project.set_property_if_unset("copy_root_files_glob", [])


@task
def package(project, logger) :
    globs = project.get_mandatory_property("copy_root_files_glob")
    if not globs :
        logger.warn("No files to copy configured. Consider removing plugin.")
        return

    source = project.basedir
    target = project.expand_path("$copy_root_files_target")
    logger.info("Copying files matching '%s' from %s to %s", " ".join(globs), source, target)

    apply_on_files(source, copy_files, globs, target, logger)


def copy_files(absolute_file_name, relative_file_name, target, logger) :
    logger.debug("Copying files %s", relative_file_name)

    parent = os.path.dirname(target)
    if not os.path.exists(parent) :
        os.makedirs(parent)
    shutil.copy(absolute_file_name, target)
