#!/bin/bash

# Get the directory of the bash script
SCRIPT_DIR=$(dirname "$0")
cd "$SCRIPT_DIR"
if [[ $# -eq 0 ]]; then
  selected_text=$(xsel)
else
  selected_text=$1
fi

# Change to the directory of the bash script
echo "$selected_text"
# Run the python file main.py with the first argument passed to the bash script
python main.py "$selected_text"