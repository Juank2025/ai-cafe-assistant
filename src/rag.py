from langchain_cohere import ChatCohere
from src.memory import ChatMemory

from src.config import CHAT_MODEL


class RAGChatbot:

    def __init__(self, vectorstore):

        self.retriever = vectorstore.as_retriever(
            search_kwargs={"k": 3}
        )

        self.llm = ChatCohere(
            model=CHAT_MODEL,
            temperature=0
        )

        self.memory = ChatMemory(max_messages=10)

    def preguntar(self, pregunta):

        documentos = self.retriever.invoke(pregunta)

        contexto = "\n\n".join(
            doc.page_content
            for doc in documentos
        )

        historial = self.memory.get_history()
        
        prompt = f"""
Eres el asistente virtual de Café Delicias del Norte.

Mantén el contexto de la conversación.

Responde únicamente utilizando la información proporcionada.

Si la información no existe responde exactamente:

"No encontré esa información en la documentación."

========================
HISTORIAL

{historial}

========================
DOCUMENTACIÓN

{contexto}

========================
PREGUNTA

{pregunta}
"""

        respuesta = self.llm.invoke(prompt)

        self.memory.add_user_message(pregunta)
        self.memory.add_ai_message(respuesta.content)

        return respuesta.content