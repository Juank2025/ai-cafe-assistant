from langchain_community.document_loaders import PyPDFLoader
from src.config import PDF_PATH

def cargar_pdf():
    loader = PyPDFLoader(PDF_PATH)
    documentos = loader.load()

    print(f"Se cargaron {len(documentos)} páginas.")

    return documentos