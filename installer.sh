#!/bin/bash

VENV_NAME = "venv"

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
python3 -m venv $VENV_NAME
source $VENV_NAME/bin/activate

echo "instalando dependencias..."
pip install -r requirements.txt

PROJECT_DIR="/home/filetransmute"
if [ ! -d "$PROJECT_DIR" ]; then
    echo "Diretório $PROJECT_DIR não encontrado. Criando o diretório..."
    mkdir -p "$PROJECT_DIR"
fi

echo "Criando o comando 'filetransmute'..." #criando o comando 'filetransmute'
echo "#!/bin/bash" | sudo tee /usr/local/bin/filetransmute
echo "python3 $PROJECT_DIR/main.py \"\$@\"" | sudo tee -a /usr/local/bin/filetransmute
sudo chmod +x /usr/local/bin/filetransmute

echo "Instalação concluida, Use 'filetransmute' para iniciar a aplicação!"

deactivate