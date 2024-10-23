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
    echo "Python já está instalado."
else
    echo "Python não encontrado. Instalando..."
    sudo apt update
    sudo apt install python3 -y
    echo "Python instalado com sucesso."
fi

if command_exists pip; then
    echo "Pip já está instalado."
else
    echo "Pip não encontrado. Instalando..."
    sudo apt install python3-pip -y
    echo "Pip instalado com sucesso."
fi

echo "Criando e ativando o ambiente virtual python..."
python3 -m venv $ENV_DIR
source $ENV_DIR/bin/activate

echo "instalando dependencias..."
pip install -r "$PROJECT_DIR/requirements.txt"


echo "Criando o comando $COMMAND_NAME..."
if [ ! -d "/usr/local/bin" ]; then
    echo "/usr/local/bin não existe. Criando o diretório..."
    sudo mkdir -p /usr/local/bin
fi

{
    echo "#!/usr/bin/env python3"
    cat "$MAIN_PY"
} | sudo tee "/usr/local/bin/$COMMAND_NAME" > /dev/null

sudo chmod +x "/usr/local/bin/$COMMAND_NAME"

echo "Instalação concluída. Use '$COMMAND_NAME' para iniciar a aplicação!"
deactivate