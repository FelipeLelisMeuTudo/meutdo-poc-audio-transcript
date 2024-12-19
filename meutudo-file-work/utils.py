import openai
from io import BytesIO
import tempfile
import os
import streamlit as st
import speech_recognition as sr
from openai import OpenAI
import re

# Create a function to transcribe audio using Whisper
def transcribe_audio(api_key, audio_file):
    openai.api_key = api_key
    client = OpenAI()
    with BytesIO(audio_file.read()) as audio_bytes:
        # Get the extension of the uploaded file
        file_extension = os.path.splitext(audio_file.name)[-1]
        
        # Create a temporary file with the uploaded audio data and the correct extension
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_audio_file:
            temp_audio_file.write(audio_bytes.read())
            temp_audio_file.seek(0)  # Move the file pointer to the beginning of the file
            
            # Transcribe the temporary audio file
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )

    return transcript

def transcribe_with_speech_recognition(audio_file_path):
    """
    Transcreve o áudio usando a biblioteca SpeechRecognition.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data, language="pt-BR")
        except sr.UnknownValueError:
            return "Não foi possível entender o áudio."
        except sr.RequestError as e:
            return f"Erro ao se comunicar com o serviço de reconhecimento: {e}"

def call_gpt(api_key, prompt, model):
    openai.api_key = api_key
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=400,
    )
    
    return response['choices'][0]['message']['content']

def call_gpt_streaming(api_key,prompt, model):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        stream=True
    )

    collected_events = []
    completion_text = ''
    placeholder = st.empty()

    for event in response:
        collected_events.append(event)
        # Check if content key exists
        if "content" in event['choices'][0]["delta"]:
            event_text = event['choices'][0]["delta"]["content"]
            completion_text += event_text
            placeholder.write(completion_text)  # Write the received text
    return completion_text

def verify_response(summary):
    regex = r'\b(empréstimo|saque|fgts)\b'

    # Verifica se as palavras estão no texto
    if re.search(regex, summary, re.IGNORECASE):
        print("O texto contém uma das palavras-chave.")
    else:
        print("O texto não contém as palavras-chave.")

def summarize_transcript(api_key, transcript, model, custom_prompt=None):
    openai.api_key = api_key
    client = OpenAI()
    prompt = f"Please summarize the following audio transcription: {transcript}"
    if custom_prompt:
        prompt = f"{custom_prompt}\n\n{transcript}"

    # Realize a chamada para a API de completions
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=150,
    )

    # Corrigido: acessar a resposta corretamente
    summary = response.choices[0].message.content
    verify_response(summary)
    return summary


def generate_image_prompt(api_key, user_input):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Create a text that explains in a lot of details how the meme about this topic would look like: {user_input}"}],
        temperature=0.7,
        max_tokens=50,
    )

    return response['choices'][0]['message']['content']

def generate_image(api_key, prompt):
    openai.api_key = api_key

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512",
        response_format="url",
    )

    return response['data'][0]['url']

def generate_images(api_key, prompt, n=4):
    openai.api_key = api_key

    response = openai.Image.create(
        prompt=prompt,
        n=n,
        size="256x256",
        response_format="url",
    )

    return response['data']