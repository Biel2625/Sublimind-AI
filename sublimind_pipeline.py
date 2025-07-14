from bark import generate_audio, SAMPLE_RATE, preload_models
from pydub import AudioSegment
import soundfile as sf
import os

# Carregar os modelos do Bark
preload_models()

# Ler as afirmações do arquivo
with open("frases.txt", "r") as file:
    texto = file.read()

# Gerar a voz com Bark
audio_array = generate_audio(texto)
sf.write("voz_bark.wav", audio_array, SAMPLE_RATE)

# Verificar se o áudio de fundo existe
fundo_path = "audio_fundo/audio_fundo.mp3"
if not os.path.exists(fundo_path):
    raise FileNotFoundError("Coloque um arquivo chamado 'audio_fundo.mp3' na pasta 'audio_fundo/'.")

# Carregar o áudio de fundo e a voz
fundo = AudioSegment.from_file(fundo_path)
voz = AudioSegment.from_file("voz_bark.wav")

# Diminuir o volume da voz para subliminar
voz_subliminar = voz - 25  # Reduz 25 dB

# Mesclar o áudio
audio_final = fundo.overlay(voz_subliminar)

# Exportar o áudio final
saida_dir = "saida"
os.makedirs(saida_dir, exist_ok=True)
saida_path = os.path.join(saida_dir, "subliminar_final.wav")
audio_final.export(saida_path, format="wav")

print(f"Áudio subliminar gerado com sucesso: {saida_path}")
