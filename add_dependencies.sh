#!/bin/bash

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Please install it first."
    exit 1
fi

# Ask for path to requirements.txt
echo "Please enter the path to your requirements.txt file: "
read -r path

# Check if path is valid
if [ ! -f "$path" ]; then
    echo "Invalid path. Please try again."
    exit 1
fi

# Add dependencies to pyproject.toml
poetry add $( cat $path )

echo "Dependencies added to pyproject.toml"