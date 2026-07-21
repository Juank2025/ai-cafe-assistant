from src.load_pdf import cargar_pdf
from src.load_excel import cargar_productos
from src.vectorstore import crear_vectorstore
from src.agent import CafeteriaAgent

print("=" * 50)
print("CAFÉ DELICIAS DEL NORTE")
print("=" * 50)

documentos = cargar_pdf()

productos = cargar_productos()

vectorstore = crear_vectorstore(documentos)

chatbot = CafeteriaAgent(vectorstore)

print("\nEscribe 'salir' para terminar.\n")

while True:

    pregunta = input("Tú: ")

    if pregunta.lower() == "salir":
        break

    respuesta = chatbot.preguntar(pregunta)

    print("\nIA:")
    print(respuesta)