import streamlit as st
import requests
import json

# Configuração da página do Streamlit
st.set_page_config(page_title="Cérebro Portátil", page_icon="🧠", layout="centered")

st.title("🧠 Meu Cérebro Portátil")
st.caption("Uma Inteligência Artificial rodando 100% offline direto do Pendrive.")

# Inicializa o histórico de mensagens no estado da sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

# Renderiza as mensagens anteriores na tela
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Captura a entrada de texto do usuário
if prompt := st.chat_input("Pergunte qualquer coisa para a sua IA..."):
    # Adiciona a mensagem do usuário ao histórico e exibe na tela
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bloco de resposta do assistente (IA)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Endereço padrão do motor Ollama rodando localmente
            url = "http://localhost:11434/api/generate"
            payload = {
                "model": "phi3",  # Modelo leve da Microsoft
                "prompt": prompt,
                "stream": True
            }
            
            # Faz a requisição de streaming para a IA responder escrevendo
            response = requests.post(url, json=payload, stream=True)
            
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line.decode('utf-8'))
                    full_response += chunk.get("response", "")
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
        except requests.exceptions.ConnectionError:
            message_placeholder.markdown("❌ **Erro:** O motor da IA (Ollama) não está respondendo. Certifique-se de ligá-lo antes de usar.")
            full_response = "Erro de conexão com o Ollama."

    # Salva a resposta da IA no histórico
    st.session_state.messages.append({"role": "assistant", "content": full_response})