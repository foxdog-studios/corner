#!/usr/bin/env zsh

setopt ERR_EXIT
setopt NO_UNSET


# ==============================================================================
# = Configuration                                                              =
# ==============================================================================

# Paths

repo=$(realpath "$(dirname "$(realpath -- $0)")/..")

venv=$repo/local/venv


# Packages

pacman_packages=(
    git
    python
    zsh
)


# ==============================================================================
# = Tasks                                                                      =
# ==============================================================================

function install_pacman_packages()
{
    sudo pacman --noconfirm --sync --needed --refresh $pacman_packages
}

function create_virtualenv()
{
    if [[ ! -d $venv ]]; then
        mkdir --parents $venv:h
        pyvenv $venv
    fi
}

function install_python_packages()
{
    unsetopt NO_UNSET
    source $venv/bin/activate
    setopt NO_UNSET

    pip install --requirement $repo/requirements.txt
}

function init_local()
{
    local config=$repo/config
    local development=$config/development

    if [[ ! -d  $development ]]; then
        cp --recursive $config/template $development
    fi

    local default=$config/default

    if [[ ! -h $default ]]; then
        $repo/scripts/config.zsh development
    fi
}


# ==============================================================================
# = Command line interface                                                     =
# ==============================================================================

tasks=(
    install_pacman_packages
    create_virtualenv
    install_python_packages
    init_local
)

function usage()
{
    cat <<-'EOF'
		Set up a development environment

		Usage:

		    setup.zsh [TASK...]

		Tasks:

		    install_pacman_packages
		    create_virtualenv
		    install_python_packages
		    init_local
	EOF
    exit 1
}

for task in $@; do
    if [[ ${tasks[(i)$task]} -gt ${#tasks} ]]; then
        usage
    fi
done

for task in ${@:-$tasks}; do
    print -P -- "%F{green}Task: $task%f"
    $task
done

