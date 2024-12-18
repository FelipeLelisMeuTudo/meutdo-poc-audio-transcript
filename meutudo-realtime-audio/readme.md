# Transcrição de Áudio em Tempo Real com Integração OpenAI

Este projeto é um aplicativo de transcrição de áudio em tempo real, construído com o framework **Textual** e a API **AsyncRealtimeConnection** da OpenAI. Ele permite que os usuários gravem áudio, enviem para um modelo GPT-4 via OpenAI e exibam as transcrições em uma interface de log rica. O aplicativo foi projetado para funcionar com um microfone, capturando áudio e enviando-o para uma sessão da OpenAI para processamento. Ele fornece uma interface simples, porém poderosa, que exibe detalhes da sessão e o status da gravação de áudio.

## Funcionalidades

- **Transcrição de Áudio em Tempo Real:** O áudio é capturado do microfone e enviado para a API da OpenAI em tempo real, onde é transcrito e exibido no aplicativo.
- **Gerenciamento de Sessão:** O aplicativo exibe o ID da sessão atual e o atualiza conforme novas sessões são criadas ou modificadas.
- **Indicador de Status de Áudio:** Um indicador visual mostra se o aplicativo está gravando áudio no momento.
- **Exibição de Log Rico:** As transcrições são exibidas em um formato de log rico, permitindo leitura fácil e atualizações dinâmicas.
- **Interação por Teclado:** Os usuários podem iniciar/parar a gravação com a tecla "K" e sair do aplicativo com a tecla "Q".

## Requisitos

- Python 3.9+
- Bibliotecas necessárias:
  - `textual` para construir a interface de usuário no terminal
  - `openai` para integração com a API da OpenAI
  - `sounddevice` para captura de áudio
  - `audio_util` para utilitários de reprodução de áudio
  - `typing_extensions` para suporte a dicas de tipo

Instale as dependências com o pip:

```bash
pip install textual openai sounddevice audio_util typing_extensions
```

## Configuração

Antes de rodar o aplicativo, verifique as seguintes configurações:

1. **Chave da API da OpenAI:** Substitua `'sua_api_key'` no código pela sua chave de API da OpenAI para autenticar a conexão.
2. **Configurações de Áudio:** O aplicativo usa as configurações padrão de áudio (canais, taxa de amostragem) definidas no módulo `audio_util`. Você pode ajustar essas configurações se necessário.

## Uso

Para iniciar o aplicativo, execute o script Python:

```bash
python realtime_app.py
```

### Controles por Teclado:
- **K:** Iniciar/parar a gravação de áudio.
- **Q:** Sair do aplicativo.

## Fluxo do Aplicativo

1. O aplicativo se conecta à API Realtime da OpenAI e cria uma nova sessão.
2. O microfone captura o áudio, que é enviado em pedaços para a API da OpenAI para transcrição.
3. As transcrições são exibidas em tempo real no painel de log rico da interface.
4. O indicador de status mostra se o aplicativo está gravando áudio ativamente.

## Visão Geral do Código

- **Widget SessionDisplay:** Exibe o ID da sessão atual.
- **Widget AudioStatusIndicator:** Exibe se o aplicativo está gravando áudio no momento.
- **Classe RealtimeApp:** Gerencia a conexão com a API Realtime da OpenAI e lida com a captura e transcrição de áudio.
- **Gravação de Áudio:** O áudio é capturado usando a biblioteca `sounddevice` e enviado para a OpenAI via conexão em tempo real.
- **Gerenciamento de Conexão em Tempo Real:** O aplicativo estabelece uma conexão WebSocket com a OpenAI, processa os dados de transcrição recebidos e envia dados de áudio.

## Personalização

Você pode personalizar as seguintes partes do aplicativo:

- **Captura de Áudio:** Modifique as configurações de captura de áudio (ex.: taxa de amostragem, canais) no módulo `audio_util`.
- **Estilo da Interface:** O aplicativo usa estilização CSS para a interface Textual. Você pode ajustar o visual e o layout modificando o bloco CSS na classe `RealtimeApp`.
- **Contexto:** O aplicativo inclui uma mensagem de contexto (`self.context_message`) que pode ser personalizada para se adequar ao seu caso de uso.
