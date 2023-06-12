#!/bin/bash

REQUIRED_PYTHON_VERSION="3.11.3"
PYTHON_COMMAND=$(python3 -c "import sys; print('True') if sys.version_info >= (3, 11, 3) else print('False')")

if [ "$PYTHON_COMMAND" != "True" ]; then
    echo "Python version must be $REQUIRED_PYTHON_VERSION or higher. Please install or update Python."
    exit
fi

# If the Python version is sufficient, the rest of the script continues

# Creates a virtual environment named "venv"
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Installing wheel
pip install wheel

# Installing dependencies with PEP 517 to avoid playsound issues
pip install --use-pep517 -r requirements.txt

# Run application
python3 src/main.py
