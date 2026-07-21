from pathlib import Path

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import (
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    VECTOR_DB_PATH
)


def crear_vectorstore(documentos):

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL
    )

    index_file = Path(VECTOR_DB_PATH) / "index.faiss"

    # Solo cargar si el índice ya existe
    if index_file.exists():

        print("\nCargando índice FAISS...")

        vectorstore = FAISS.load_local(
            str(VECTOR_DB_PATH),
            embeddings,
            allow_dangerous_deserialization=True
        )

        print("Índice cargado correctamente.")

        return vectorstore

    print("\nCreando nuevo índice FAISS...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documentos)

    print(f"Se generaron {len(chunks)} fragmentos.")

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    # Crear la carpeta si no existe
    Path(VECTOR_DB_PATH).mkdir(parents=True, exist_ok=True)

    vectorstore.save_local(str(VECTOR_DB_PATH))

    print("Índice guardado correctamente.")

    return vectorstore