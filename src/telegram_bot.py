from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

from src.config import TELEGRAM_TOKEN
from src.agent import CafeteriaAgent


class TelegramBot:

    def __init__(self, vectorstore):
        self.agent = CafeteriaAgent(vectorstore)

    async def responder(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ):
        mensaje = update.message.text

        respuesta = self.agent.preguntar(
            mensaje
        )

        await update.message.reply_text(
            respuesta
        )

    async def inicio(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ):
        await update.message.reply_text(
            """
☕ Bienvenido a Café Delicias del Norte.

Puedes preguntarme sobre:

- Horarios
- Productos
- Precios
- Trabajadores
- Políticas de la cafetería

¿Cómo puedo ayudarte?
"""
        )

    def ejecutar(self):
        # URL del proxy requerido por la cuenta gratuita de PythonAnywhere
        PROXY_URL = "http://proxy.server:3128"

        app = Application.builder()\
            .token(TELEGRAM_TOKEN)\
            .proxy_url(PROXY_URL)\
            .get_updates_proxy_url(PROXY_URL)\
            .build()

        app.add_handler(
            CommandHandler(
                "start",
                self.inicio
            )
        )

        app.add_handler(
            MessageHandler(
                filters.TEXT,
                self.responder
            )
        )

        print("Bot Telegram iniciado...")

        app.run_polling()