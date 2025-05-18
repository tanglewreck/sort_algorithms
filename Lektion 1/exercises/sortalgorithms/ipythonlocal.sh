#!/usr/bin/env bash
# shellcheck shell=bash
# Start ipython using a local .ipython
IPYTHONDIR_="$(pwd)/.ipython"
if [ -d "$IPYTHONDIR_" ]; then
    IPYTHONDIR="$IPYTHONDIR_" ipython --pylab
else
    echo "No .ipython in the current directory: FAIL"
    exit 1
fi
exit 0
