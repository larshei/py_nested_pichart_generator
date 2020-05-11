#!/bin/bash

# functions {{{ #
function create_virtual_env() {
    echo "Creating virtual environment"
    python3 -m venv venv
}


function activate_virtual_environment() {
    echo "Activating virtual environment"
    source ./venv/bin/activate
}


function install_requirements() {
    echo "Installing required packages"
    python3 -m pip install -r requirements.txt
}


function check_prerequisites() {
    # Check for python installed  {{{ #
    if brew list python > /dev/null 2>&1; then
        echo "Python is already installed"
    else
        brew install python
    fi
    # }}} Check for python installed  #

    # create config {{{ #
    mkdir -p instance
    touch instance/config.py
    # }}} create config #
}
# }}} functions #


function main() {
    check_prerequisites
    create_virtual_env
    activate_virtual_environment
    install_requirements
}


main
