import streamlit as st
import openai
import speech_recognition as sr
import os
from utils import transcribe_with_speech_recognition, transcribe_audio, summarize_transcript
import theme

# Streamlit app setup
st.set_page_config(**theme.page_config)

title = """
    <h1 style="color:#32CD32; font-family:sans-serif;">🎙️ Meutudo audio transcript 🎙️</h1>
"""
st.markdown(title, unsafe_allow_html=True)
st.write("Carregue um arquivo de áudio, transcreva-o usando o modelo selecionado e resuma a transcrição.")

api_key = 'api_key'
models = ["gpt-4o", "gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4-0613", "gpt-4o-2024-11-20", "gpt-4o-audio-preview", "gpt-4o-2024-05-13"]
model = st.selectbox("Selecione um modelo:", models)

uploaded_audio = st.file_uploader("Carregar um arquivo de áudio", type=['m4a', 'mp3', 'webm', 'mp4', 'mpga', 'wav', 'mpeg'], accept_multiple_files=False)

custom_prompt = None
custom_prompt = st.text_input("Insira um prompt personalizado:", value="Responda em português brasileiro")


if st.button("Transcrever"):
    if uploaded_audio:
        if api_key:
            # Save the uploaded audio temporarily
            temp_file_path = f"temp_{uploaded_audio.name}"
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(uploaded_audio.read())

            st.markdown("Transcribing the audio...")

            with open(temp_file_path, "rb") as audio_file:
                transcript = transcribe_audio(api_key, audio_file)

            # Show the transcription
            st.markdown(f"###  Transcription:\n\n<details><summary>Click to view</summary><p><pre><code>{transcript}</code></pre></p></details>", unsafe_allow_html=True)

            st.markdown("Summarizing the transcription...")

            # Summarize using the OpenAI API
            if custom_prompt:
                summary = summarize_transcript(api_key, transcript, model, custom_prompt)
            else:
                summary = summarize_transcript(api_key, transcript, model)
            
            st.markdown(f"### Summary:")
            st.write(summary)

            # Clean up temporary file
            os.remove(temp_file_path)
        else:
            st.error("Please enter a valid OpenAI API key.")
