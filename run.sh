#!/bin/bash

# Get the directory of the bash script
SCRIPT_DIR=$(dirname "$0")

# Change to the directory of the bash script
cd "$SCRIPT_DIR"

# Run the python file main.py with the first argument passed to the bash script
python main.py "$1"