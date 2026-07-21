from langchain_core.tools import tool

from src.product_search import buscar_producto


def crear_tools(vectorstore):


    @tool
    def consultar_producto(producto: str):
        """
        Busca productos y precios disponibles en el catálogo Excel.
        """

        return buscar_producto(producto)



    @tool
    def consultar_politicas(pregunta: str):
        """
        Consulta información general de la cafetería:
        horarios, trabajadores, salarios,
        beneficios, formas de pago, etc.
        """

        documentos = vectorstore.similarity_search(
            pregunta,
            k=3
        )


        if not documentos:
            return "No encontré información."


        contexto = "\n\n".join(
            doc.page_content
            for doc in documentos
        )


        return contexto


    return [
        consultar_producto,
        consultar_politicas
    ]