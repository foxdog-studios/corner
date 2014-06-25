#!/usr/bin/env zsh

setopt ERR_EXIT
setopt NO_UNSET

repo=$(realpath "$(dirname "$(realpath -- $0)")/..")

if ! (( $+CORNER_CONFIG )); then
    export CORNER_CONFIG=$repo/config/default/corner.json
fi

if [[ $# -eq 0 ]]; then
    args=(
        $repo/data/Cornerhouse-films-screened-since-Nov-1999.csv
        $repo/local/output
    )
else
    args=( $@ )
fi

unsetopt NO_UNSET
source $repo/local/venv/bin/activate
setopt NO_UNSET

PYTHONPATH=$repo python -m corner $args

