#!/usr/bin/env bash

repo=$(readlink -f "$(dirname "$(readlink -f -- "${BASH_SOURCE[0]}")")/..")
export PYTHONPATH=$repo
python -m corner "$@"

