# Consulta Inteligente a Documentos com Ollama e ChromaDB

Este projeto permite carregar documentos PDF, extrair seu conteúdo e realizar consultas inteligentes utilizando embeddings de IA. Ele utiliza as seguintes tecnologias:

- **Ollama** para geração de embeddings
- **ChromaDB** para armazenamento e consulta vetorial
- **Streamlit** para interface web
- **PyPDF2** para extração de texto de PDFs

## 🚀 Como configurar e executar

### 1. Pré-requisitos

Antes de começar, instale as dependências executando:

```sh
pip install -r requirements.txt
```

### 2. Executando o projeto
Para rodar a aplicação, execute:

```sh
Copiar
Editar
streamlit run app.py
```

Isso iniciará uma interface web onde você poderá fazer upload de PDFs e realizar consultas.

#### 📌 Como funciona?
O usuário faz upload de um arquivo PDF.

O texto é extraído e dividido em trechos menores.

Cada trecho é armazenado no ChromaDB com seus respectivos embeddings gerados pelo Ollama.

O usuário pode digitar perguntas sobre o conteúdo do documento, e o sistema retorna os trechos mais relevantes.

#### 🛠 Tecnologias utilizadas
Python

Ollama

ChromaDB

LangChain (módulo OllamaEmbeddings)

Streamlit

PyPDF2

#### 📄 Licença

Este projeto é de código aberto e pode ser modificado conforme necessário.
