
from langchain_community.embeddings import OllamaEmbeddings
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings


class OllamaEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        self.ollama_embeddings = OllamaEmbeddings(
            model="mistral",
            base_url="http://localhost:11434"
        )

    def __call__(self, texts: Documents) -> Embeddings:
        # Converter para lista se não for
        if isinstance(texts, str):
            texts = [texts]

        embeddings = self.ollama_embeddings.embed_documents(texts)
        return embeddings