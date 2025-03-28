from unittest.mock import MagicMock, patch

import pytest

from PdfUtils import extract_text_from_pdf


@pytest.fixture
def mock_pdf_reader():
    """Mock da classe PdfReader para simular diferentes cenários."""
    with patch("PyPDF2.PdfReader") as MockReader:
        yield MockReader


def test_extract_text_from_pdf_multiple_pages(mock_pdf_reader):
    """Testa a extração de texto de um PDF com múltiplas páginas."""
    mock_pdf = MagicMock()
    mock_pdf.pages = [MagicMock(), MagicMock()]
    mock_pdf.pages[0].extract_text.return_value = "Texto da página 1."
    mock_pdf.pages[1].extract_text.return_value = "Texto da página 2."

    mock_pdf_reader.return_value = mock_pdf

    result = extract_text_from_pdf("dummy.pdf")

    assert result


def test_extract_text_from_pdf_empty(mock_pdf_reader):
    """Testa um PDF sem texto (vazio)."""
    mock_pdf = MagicMock()
    mock_pdf.pages = []

    mock_pdf_reader.return_value = mock_pdf

    result = extract_text_from_pdf("dummy.pdf")

    assert result == []


def test_extract_text_from_pdf_whitespace(mock_pdf_reader):
    """Testa um PDF contendo apenas espaços em branco e quebras de linha."""
    mock_pdf = MagicMock()
    mock_pdf.pages = [MagicMock()]
    mock_pdf.pages[0].extract_text.return_value = "   \n   \n"

    mock_pdf_reader.return_value = mock_pdf

    result = extract_text_from_pdf("dummy.pdf")

    assert result == []


def test_extract_text_from_pdf_file_not_found():
    """Testa se a função levanta um erro ao tentar ler um arquivo inexistente."""
    with pytest.raises(FileNotFoundError):
        extract_text_from_pdf("arquivo_inexistente.pdf")
