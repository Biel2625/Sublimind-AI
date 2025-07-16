import streamlit as st
from bark import generate_audio, SAMPLE_RATE, preload_models
from pydub import AudioSegment
import soundfile as sf
import os

st.set_page_config(page_title="Sublimind AI", page_icon="🔊")
st.title("🔊 Sublimind AI - Áudio Subliminar Automático")

# Campo de texto para as afirmações
afirmacoes = st.text_area("✍️ Digite suas afirmações subliminares abaixo:", 
"""Eu sou calmo e confiante.
Minha mente atrai prosperidade.
Eu tenho foco total nas minhas metas.""")

# Upload do áudio de fundo
audio_fundo = st.file_uploader("🔊 Faça upload do áudio de fundo (Altas Frequências)", type=["mp3", "wav"])

# Botão para gerar o áudio subliminar
if st.button("🚀 Gerar Áudio Subliminar"):
    if afirmacoes.strip() == "":
        st.error("Por favor, digite as afirmações.")
    elif audio_fundo is None:
        st.error("Por favor, faça o upload do áudio de fundo.")
    else:
        with st.spinner("Gerando áudio subliminar..."):

            # Preparar pastas
            os.makedirs("saida", exist_ok=True)

            # Salvar o áudio de fundo temporário
            fundo_path = "audio_fundo_temp.mp3"
            with open(fundo_path, "wb") as f:
                f.write(audio_fundo.read())

            # Carregar Bark
            preload_models()

            # Gerar voz com Bark
            audio_array = generate_audio(afirmacoes)
            sf.write("voz_bark.wav", audio_array, SAMPLE_RATE)

            # Carregar áudios
            fundo = AudioSegment.from_file(fundo_path)
            voz = AudioSegment.from_file("voz_bark.wav")

            # Reduzir o volume da voz para subliminar
            voz_subliminar = voz - 25

            # Mesclar a voz com o áudio de fundo
            audio_final = fundo.overlay(voz_subliminar)

            # Exportar o áudio final
            output_path = "saida/subliminar_final.wav"
            audio_final.export(output_path, format="wav")

            st.success("✅ Áudio subliminar gerado com sucesso!")

            # Download do arquivo
            with open(output_path, "rb") as f:
                st.download_button("📥 Baixar Áudio Subliminar", f, file_name="subliminar_final.wav")
