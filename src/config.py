from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

PDF_PATH = BASE_DIR / "documentos" / "cafeteria.pdf"
EXCEL_PATH = BASE_DIR / "documentos" / "productos.xlsx"

CHAT_MODEL = "command-a-03-2025"

EMBEDDING_MODEL = "models/gemini-embedding-001"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

VECTOR_DB_PATH = BASE_DIR / "data" / "faiss_index"

TELEGRAM_TOKEN = os.getenv(
    "TELEGRAM_TOKEN"
)