import unittest
from unittest.mock import MagicMock

import pytest
from langchain_community.embeddings import OllamaEmbeddings

from OllamaEmbeddingFunction import OllamaEmbeddingFunction


class TestOllamaEmbeddingFunction(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para os testes."""
        self.embedding_function = OllamaEmbeddingFunction()
        self.embedding_function.ollama_embeddings = MagicMock(spec=OllamaEmbeddings)

    def test_embedding_single_text(self):
        """Testa se a função de embeddings funciona corretamente com um único texto."""
        text = "Teste de embedding"
        fake_embedding = [[0.1, 0.2, 0.3]]

        # Mockando o método embed_documents
        self.embedding_function.ollama_embeddings.embed_documents.return_value = fake_embedding

        result = self.embedding_function(text)

        assert result

    def test_embedding_multiple_texts(self):
        """Testa se a função de embeddings funciona corretamente com múltiplos textos."""
        texts = ["Texto 1", "Texto 2"]
        fake_embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]

        # Mockando o método embed_documents
        self.embedding_function.ollama_embeddings.embed_documents.return_value = fake_embeddings

        result = self.embedding_function(texts)

        assert result

    def test_embedding_empty_input(self):
        """Testa se a função levanta um ValueError quando recebe uma entrada vazia."""
        texts = []

        self.embedding_function.ollama_embeddings.embed_documents.return_value = []

        with pytest.raises(ValueError):
            self.embedding_function(texts)


if __name__ == "__main__":
    unittest.main()
