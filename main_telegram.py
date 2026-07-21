from src.load_pdf import cargar_pdf
from src.vectorstore import crear_vectorstore
from src.telegram_bot import TelegramBot


print("="*50)
print("CAFÉ DELICIAS DEL NORTE")
print("="*50)


documentos = cargar_pdf()


vectorstore = crear_vectorstore(
    documentos
)


bot = TelegramBot(
    vectorstore
)


bot.ejecutar()