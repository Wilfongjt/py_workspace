#!/bin/sh
set -o allexport
source .env set
set +o allexport
python3 ./lib/git.branch.py
