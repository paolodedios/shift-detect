# -*- c-file-style: "sourcery" -*-
#
# Use and distribution of this software and its source code is governed
# by the terms and conditions defined in the "LICENSE" file that is part
# of this source code package.
"""
PyBuilder devpi plugin
"""
import os
import subprocess

from pybuilder.core   import use_plugin
from pybuilder.core   import init
from pybuilder.core   import task
from pybuilder.core   import description
from pybuilder.core   import depends
from pybuilder.errors import BuildFailedException
from pybuilder.utils  import assert_can_execute

use_plugin("python.core")

@init
def initialize_devpi_plugin(project) :
    project.set_property_if_unset("devpi_user"         , "root")
    project.set_property_if_unset("devpi_staging_index", "root")
    project.set_property_if_unset("devpi_release_index", "root")


@task("stage")
@depends("publish")
@description("Upload packaged distribution to devpi server's staging index")
def upload_distribution(project, logger) :
    project.build_depends_on("devpi")
    assert_can_execute(["devpi", "--version"], prerequisite="devpi PyPi Server", caller="devpi_plugin")

    index_name = "{}/{}".format(project.get_property("devpi_user"), project.get_property("devpi_staging_index"))

    logger.info("Uploading binary distribution in %s to staging index %s", project.expand_path("$dir_dist"), index_name)

    run_devpi_command(project, logger, ["login", project.get_property("devpi_user"), "--password="])
    run_devpi_command(project, logger, ["use", project.get_property("devpi_staging_index")])
    run_devpi_command(project, logger, ["upload", "--no-vcs", "--formats=bdist_wheel,bdist_egg"])


@task("release")
@depends("stage")
@description("Push uploaded distribution to devpi server's release index from its staging index")
def push_distribution(project, logger) :
    project.build_depends_on("devpi")
    assert_can_execute(["devpi", "--version"], prerequisite="devpi PyPi Server", caller="devpi_plugin")

    distribution_name = "{}-{}".format(project.name, project.version)
    index_name        = "{}/{}".format(project.get_property("devpi_user"), project.get_property("devpi_release_index"))

    logger.info("Pushing binary distribution %s to release index %s", distribution_name, index_name)

    run_devpi_command(project, logger, ["login", project.get_property("devpi_user"), "--password="])
    run_devpi_command(project, logger, ["use", project.get_property("devpi_release_index")])
    run_devpi_command(project, logger, ["push", distribution_name, index_name])


def run_devpi_command(project, logger, params) :
    reports_dir = project.expand_path("$dir_reports/devpi")
    if not os.path.exists(reports_dir) :
        os.mkdir(reports_dir)

    logger.debug("Executing devpi command %s", params)

    output_file_path = os.path.join(reports_dir, params[0].replace("/", ""))

    with open(output_file_path, "w") as output_file :
        commandexec = ["devpi"]
        commandexec.extend(params)
        working_dir = project.expand_path("$dir_dist")
        process     = subprocess.Popen(commandexec, cwd=working_dir, stdout=output_file, stderr=output_file, shell=False)
        return_code = process.wait()
        if return_code != 0 :
            raise BuildFailedException("Error while executing devpi command %s, see %s for details" % (params, output_file_path))
