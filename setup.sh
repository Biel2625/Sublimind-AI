#!/bin/bash

# Atualizar pacotes e instalar FFmpeg
apt update && apt install -y ffmpeg

# Instalar Bark direto do repositório
pip install git+https://github.com/suno-ai/bark.git

# Instalar dependências adicionais
pip install pydub soundfile

echo "Setup concluído: Bark + FFmpeg instalados!"
