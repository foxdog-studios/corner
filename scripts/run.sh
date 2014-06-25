#!/usr/bin/env bash

repo=$(readlink -f "$(dirname "$(readlink -f -- "${BASH_SOURCE[0]}")")/..")

if [[ $# -eq 0 ]]; then
    args=(
        'data/Cornerhouse-films-screened-since-Nov-1999.csv'
        'output'
    )
else
    args=( "$@" )
fi

PYTHONPATH=$repo python -m corner "${args[@]}"

