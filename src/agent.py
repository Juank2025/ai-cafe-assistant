from langchain.agents import create_agent

from langchain_cohere import ChatCohere

from src.config import CHAT_MODEL
from src.tools import crear_tools



class CafeteriaAgent:


    def __init__(self, vectorstore):


        self.llm = ChatCohere(
            model=CHAT_MODEL,
            temperature=0
        )


        tools = crear_tools(vectorstore)


        self.agent = create_agent(
            model=self.llm,
            tools=tools,
            system_prompt="""
Eres el asistente virtual de Café Delicias del Norte.

Tu trabajo es responder preguntas de clientes
y empleados.

Reglas:

- Si preguntan por precios, productos o valores,
  utiliza consultar_producto.

- Si preguntan por horarios, trabajadores,
  salarios, políticas o información general,
  utiliza consultar_politicas.

- No inventes información.

- Si no encuentras información responde:
  "No tengo información disponible."
"""
        )



    def preguntar(self, mensaje):


        respuesta = self.agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": mensaje
                    }
                ]
            }
        )


        return respuesta["messages"][-1].content