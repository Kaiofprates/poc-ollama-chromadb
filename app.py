import os

import chromadb
import streamlit as st

from OllamaEmbeddingFunction import OllamaEmbeddingFunction
from PdfUtils import extract_text_from_pdf

# Configurar o Chroma
chroma_client = chromadb.Client()

# Criar o embedding function customizado
embedding_function = OllamaEmbeddingFunction()

# Criar ou obter a collection
collection_name = "manual_pix"

try:
    collection = chroma_client.create_collection(
        name=collection_name,
        embedding_function=embedding_function
    )
except:
    collection = chroma_client.get_collection(
        name=collection_name,
        embedding_function=embedding_function
    )

# Interface Streamlit
st.title("Consulta Inteligente a Documentos")

# Upload do arquivo PDF
uploaded_file = st.file_uploader("Faça upload de um arquivo PDF", type=['pdf'])

if uploaded_file is not None:
    # Salvar o arquivo temporariamente
    with open("temp_document.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())

    # Extrair texto e adicionar à collection
    documents = extract_text_from_pdf("temp_document.pdf")

    # Adicionar documentos à collection com IDs únicos
    collection.add(
        documents=documents,
        ids=[f"id_{i}" for i in range(len(documents))]
    )

    st.success("Documento carregado com sucesso!")

    # Remover arquivo temporário
    os.remove("temp_document.pdf")

# Interface para consultas
query = st.text_input("Digite sua pergunta sobre o documento:")

if query:
    # Realizar a consulta
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    # Mostrar resultados
    st.subheader("Respostas encontradas:")
    for i, doc in enumerate(results['documents'][0]):
        st.write(f"Resposta {i + 1}:")
        st.write(doc)
        st.write("---")
