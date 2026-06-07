# 🤖 Projeto Cérebro Portátil (IA no Pendrive)

Este projeto transforma um pendrive comum em um assistente de Inteligência Artificial portátil que roda localmente, sem precisar de internet e mantendo total privacidade dos seus dados.

## 🛠️ Tecnologias Utilizadas
* **Python**: Base do ecossistema do projeto.
* **Streamlit**: Interface gráfica limpa executada direto no navegador.
* **Ollama**: Motor local para execução de LLMs compactos.
* **Phi-3 (Microsoft)**: Modelo de linguagem eficiente rodando offline.

## 🚀 Como Preparar e Usar o seu Pendrive

### 1. Formatação do Hardware
Certifique-se de formatar o seu pendrive (mínimo de 16GB, recomendado USB 3.0 para maior velocidade) usando o sistema de arquivos **NTFS** ou **exFAT**. O formato padrão FAT32 impede o armazenamento de arquivos maiores que 4GB (limitação crítica para modelos de IA).

### 2. Clonando a Estrutura
Baixe os arquivos deste repositório (`app.py`, `requirements.txt`, `ligar.bat` e `README.md`) para dentro de uma pasta no seu pendrive.

### 3. Configurando o Motor da IA (Ollama)
1. Instale o **Ollama** no computador host a partir do site oficial (ollama.com).
2. Para carregar e salvar os modelos diretamente no pendrive (evitando consumir espaço no disco rígido principal do PC), configure a variável de ambiente do sistema digitando no terminal:
   ```bash
   setx OLLAMA_MODELS "E:\OllamaModels"
