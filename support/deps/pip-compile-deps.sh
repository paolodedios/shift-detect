#!/bin/bash -e
#
# Generate pip requirements.txt specification for build and runtime dependencies
#
################################################################################

################################################################################
#
# Output variables
#
################################################################################

PIP_COMPILER_BUILD_DEPS_OUTFILE=requirements-build.txt
PIP_COMPILER_RUNTIME_DEPS_OUTFILE=requirements.txt

################################################################################
#
# Input variables
#
################################################################################

PIP_COMPILER_BUILD_DEPS_INFILE=requirements-build.in
PIP_COMPILER_RUNTIME_DEPS_INFILE=requirements-runtime.in


function compile_requirements()
{
    echo "Generating build dependencies list from [$PIP_COMPILER_BUILD_DEPS_INFILE]"
    pip-compile -v --no-index -o $PIP_COMPILER_BUILD_DEPS_OUTFILE $PIP_COMPILER_BUILD_DEPS_INFILE

    echo "Generating runtime dependencies list from [$PIP_COMPILER_RUNTIME_DEPS_INFILE]"
    pip-compile -v --no-index -o $PIP_COMPILER_RUNTIME_DEPS_OUTFILE $PIP_COMPILER_RUNTIME_DEPS_INFILE
}


function sync_requirements()
{
    echo "Synchronizing environment with dependency specifications"

    pip-sync $PIP_COMPILER_BUILD_DEPS_OUTFILE $PIP_COMPILER_RUNTIME_DEPS_OUTFILE
}


if [ $# -eq 1 ]; then
    PIP_COMPILER_BUILD_DIRECTORY="$1"
else
    echo "Missing source directory argument."
    PIP_COMPILER_BUILD_DIRECTORY=
    exit 1
fi

case "$PIP_BUILD_ENV" in

    dev|devel|debug)
        cd $PIP_COMPILER_BUILD_DIRECTORY

        PIP_COMPILER_BUILD_DEPS_INFILE=requirements-dev-build.in
        PIP_COMPILER_RUNTIME_DEPS_INFILE=requirements-dev-runtime.in

        compile_requirements
        ;;

    sync)
        cd $PIP_COMPILER_BUILD_DIRECTORY

        sync_requirements
        ;;
    *)
        cd $PIP_COMPILER_BUILD_DIRECTORY

        PIP_COMPILER_BUILD_DEPS_INFILE=requirements-prod-build.in
        PIP_COMPILER_RUNTIME_DEPS_INFILE=requirements-prod-runtime.in

        compile_requirements
        ;;

esac
