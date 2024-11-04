#!/bin/bash

ENV_DIR="env"
PROJECT_DIR="$(pwd)"
VENV_DIR="$PROJECT_DIR/venv"
MAIN_PY="$PROJECT_DIR/main.py"
COMMAND_NAME="filetransmute"

command_exists() { # função que verifica se um comando existe
    command -v "$1" >/dev/null 2>&1
}

if command_exists python3; then
    echo "Python already installed"
else
    echo "Python not found. Installing..."
    sudo apt update
    sudo apt install python3 -y
    echo "Python successfully installed"
fi

if command_exists pip; then
    echo "Pip already installed."
else
    echo "Pip not found. Installing..."
    sudo apt install python3-pip -y
    echo "Pip successfully installed."
fi

echo "Creating and activing a python virtual env..."
python3 -m venv $ENV_DIR
source $ENV_DIR/bin/activate

echo "Installing depedencies..."
pip install -r "$PROJECT_DIR/requirements.txt"


echo "Creating the command $COMMAND_NAME..."
if [ ! -d "/usr/local/bin" ]; then
    echo "/usr/local/bin do not exist. Creating a directory..."
    sudo mkdir -p /usr/local/bin
fi

{
    echo "#!/usr/bin/env python3"
    cat "$MAIN_PY"
} | sudo tee "/usr/local/bin/$COMMAND_NAME" > /dev/null

sudo chmod +x "/usr/local/bin/$COMMAND_NAME"

echo "Installation finished. Use '$COMMAND_NAME' to launch the application!"
deactivate