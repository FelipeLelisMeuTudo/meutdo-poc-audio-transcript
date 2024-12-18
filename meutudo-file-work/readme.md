Aqui está um modelo de README para o seu projeto:

---

# **Audio Transcription and Summarization**

Este projeto é um aplicativo web desenvolvido com Streamlit para transcrição de áudio e sumarização utilizando modelos da OpenAI, como Whisper e GPT-3.5. O objetivo é permitir que os usuários carreguem arquivos de áudio, transcrevam seu conteúdo e recebam um resumo gerado automaticamente pela IA.

## **Recursos**
- **Transcrição de Áudio**: Utiliza os modelos de transcrição da OpenAI (Whisper) ou a biblioteca SpeechRecognition para transcrever áudio para texto.
- **Sumarização de Texto**: Após a transcrição, o texto pode ser resumido usando modelos GPT-3.5 ou GPT-4.
- **Interface Interativa**: Interface simples e intuitiva utilizando Streamlit para facilitar o upload de arquivos, seleção de métodos e visualização de resultados.

## **Como Funciona**
1. **Upload de Arquivo de Áudio**: O usuário envia um arquivo de áudio (formato WAV, MP3, M4A, entre outros).
2. **Seleção de Método de Transcrição**:
    - **SpeechRecognition**: Usando a biblioteca `speech_recognition` e o Google Speech-to-Text.
    - **Whisper**: Utilizando o modelo de transcrição da OpenAI Whisper.
3. **Exibição da Transcrição**: Após a transcrição do áudio, o texto é exibido no aplicativo.
4. **Sumarização do Texto**: O usuário pode escolher gerar um resumo do texto transcrito, usando o modelo GPT-3.5 ou GPT-4.
5. **Respostas Interativas**: O resumo pode ser personalizado com um prompt específico fornecido pelo usuário.

## **Tecnologias Utilizadas**
- **Streamlit**: Para criar a interface do usuário de forma rápida e interativa.
- **OpenAI API**: Para transcrição com Whisper e sumarização com GPT-3.5 / GPT-4.
- **SpeechRecognition**: Para transcrição de áudio com o Google Speech-to-Text.
- **Python**: A linguagem principal usada para desenvolvimento.
- **IO**: Para manipulação de arquivos em memória.

## **Pré-requisitos**
- Python 3.7 ou superior.
- Conta na OpenAI e chave de API válida.

## **Instalação**
1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/audio-transcr.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd audio-transcr
   ```
3. Crie um ambiente virtual e ative-o (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para sistemas Unix
   venv\Scripts\activate     # Para Windows
   ```
4. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

## **Chave da API OpenAI**
O projeto utiliza a API da OpenAI para transcrição e sumarização. Para usar o projeto, você precisa de uma chave de API da OpenAI:
1. Crie uma conta na [OpenAI](https://platform.openai.com/signup).
2. Gere sua chave de API na [página de API da OpenAI](https://platform.openai.com/account/api-keys).
3. Insira a chave da API no campo correspondente do aplicativo.

## **Como Usar**
1. Execute o aplicativo Streamlit:
   ```bash
   streamlit run app.py
   ```
2. O aplicativo será aberto no navegador, onde você poderá:
   - Fazer upload de um arquivo de áudio.
   - Escolher o método de transcrição (SpeechRecognition ou Whisper).
   - Visualizar o texto transcrito.
   - Gerar e visualizar o resumo do texto transcrito.
   
## **Exemplo de Uso**
1. Faça o upload de um arquivo de áudio no formato WAV ou MP3.
2. Selecione o método de transcrição desejado.
3. O aplicativo irá transcrever o áudio e mostrar o texto.
4. Você pode solicitar um resumo do texto transcrito, que será gerado automaticamente pela IA.

## **Personalização**
- **Prompt Customizado**: Você pode fornecer um prompt específico para orientar a sumarização.
- **Modelos da OpenAI**: É possível selecionar entre os modelos GPT-3.5 ou GPT-4 para realizar a sumarização.

## **Dependências**
- **openai**: Para integração com a API da OpenAI.
- **streamlit**: Para a interface de usuário.
- **speechrecognition**: Para transcrição de áudio utilizando o Google Speech-to-Text.
- **pydub**: Para manipulação de arquivos de áudio.
- **io**: Para manipulação de arquivos em memória.

Instale as dependências com o seguinte comando:

```bash
pip install openai streamlit speechrecognition pydub
```