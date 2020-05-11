#!/bin/bash

echo "activating virtual environment"
source ./venv/bin/activate

python3 -m pip freeze > requirements.txt
