#!/bin/bash

# Get the directory of the bash script
SCRIPT_DIR=$(dirname "$0")
selected_text=$(xsel)
# Change to the directory of the bash script
cd "$SCRIPT_DIR"

# Run the python file main.py with the first argument passed to the bash script
python main.py "$selected_text"