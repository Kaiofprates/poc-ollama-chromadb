import PyPDF2

# Função para extrair texto do PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"

    # Dividir o texto em chunks menores (por exemplo, por parágrafos)
    chunks = text.split('\n\n')
    return [chunk.strip() for chunk in chunks if chunk.strip()]