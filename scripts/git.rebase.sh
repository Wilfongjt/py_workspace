#!/bin/sh
set -o allexport
source git.rebase.env set
set +o allexport
python3 ../../../../_tools/lib/git.rebase.py

