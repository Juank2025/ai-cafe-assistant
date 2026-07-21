# ☕ Café Delicias del Norte - Agente IA con LangChain (RAG)

Un chatbot inteligente desarrollado en Python utilizando **LangChain, Cohere, FAISS y Telegram Bot API**, capaz de responder consultas sobre una cafetería utilizando la técnica **RAG** (*Retrieval-Augmented Generation*).

---

## 📸 Demostración y Despliegue

### 🤖 Bot de Telegram en Producción (AWS EC2)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fafa20e5-be3c-4530-b232-64c2d0070dc0" />


### ⚙️ Ejecución Local y Pruebas por Consola
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1618a9e3-b657-4cb4-b4d9-aaf8226ae80b" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f65a0a7e-cf60-42d2-a114-1c5e7d72bff5" />



### ☁️ Servidor de Despliegue en AWS
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b70c0393-c740-41f2-afaa-42eafc02c289" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2597ce19-dc84-4a98-ab0b-5200b986815b" />
---

## 🚀 Características

- 📄 **Consultas desde documentos:** Extrae y procesa información desde archivos PDF.
- 📊 **Carga de Datos Estructurados:** Procesa catálogo de productos y precios desde archivos Excel.
- 🧠 **Búsqueda Semántica:** Implementa RAG con FAISS para indexación y recuperación precisa de contexto.
- 🤖 **Respuestas Inteligentes:** Integra LLM de **Cohere** y Embeddings con **Google Generative AI / Cohere**.
- 💬 **Canal Telegram:** Despliegue con bot en producción mediante `python-telegram-bot`.
- ☁️ **Despliegue 24/7:** Configurado como servicio de sistema (`systemd`) en una instancia **AWS EC2 (Ubuntu)**.

---
´´´
## 🏗️ Arquitectura del Sistema

Usuario (Telegram)
       │
       ▼
Bot Telegram API
       │
       ▼
Agente IA (LangChain)
       │
  ┌────┴─────────────────┐
  ▼                      ▼
FAISS Vector Store    Productos (Excel)
  │
  ▼
Información PDF
´´´
---

## 📂 Estructura del proyecto
´´´
ai-cafe-assistant/
│
├── documentos/
│   ├── cafeteria.pdf
│   └── productos.xlsx
│
├── data/
│   └── faiss_index/         # Índice vectorial generado por FAISS
│
├── src/
│   ├── agent.py
│   ├── config.py
│   ├── excel_loader.py
│   ├── load_pdf.py
│   ├── rag.py
│   └── vectorstore.py
│
├── main.py                  # Ejecución interactiva por consola local
├── main_telegram.py         # Entrypoint del Bot de Telegram
├── requirements.txt         # Dependencias del proyecto
├── .env                     # Variables de entorno (API Keys)
└── README.md
´´´
## 🛠️ Tecnologías utilizadas

- Lenguaje: Python 3.12 / 3.13

- Framework de IA: LangChain

- LLM & Embeddings: Cohere API & Google Generative AI Embeddings

- Base de Datos Vectorial: FAISS

- Procesamiento de Datos: Pandas, PyPDF

- Integración: python-telegram-bot

- Infraestructura: AWS EC2 (Ubuntu 24.04 LTS + Systemd)

---

## ⚙️ Instalación y Configuración Local

1. Clonar el repositorio
   git clone [https://github.com/Juank2025/ai-cafe-assistant.git](https://github.com/Juank2025/ai-cafe-assistant.git)
   cd ai-cafe-assistant

2. Crear y activar el entorno virtual
   python3 -m venv venv
   source venv/bin/activate

3. Instalar dependencias
   pip install -r requirements.txt

🔑 Variables de Entorno

Crear un archivo .env en la raiz del proyecto con la estructura:

TELEGRAM_TOKEN=tu_telegram_bot_token
COHERE_API_KEY=tu_api_key_de_cohere
GOOGLE_API_KEY=tu_api_key_de_google

▶️ Modos de Ejecución

Pruebas locales:
python main_telegram.py

☁️ Despliegue en Producción (AWS EC2)
El bot se encuentra desplegado en una instancia Ubuntu Server de AWS EC2 y se gestiona mediante Systemd para asegurar disponibilidad continua.

# Verificar estado del bot en la instancia
sudo systemctl status cafebot

# Monitorear logs en tiempo real
journalctl -u cafebot -f

💬 Ejemplos de Preguntas que responde el Bot
¿Cuál es el horario de atención?

¿Aceptan pagos con tarjeta de crédito/débito?

¿Cuánto cuesta un Café Latte y qué postres tienen?

¿Tienen conexión WiFi disponible?

¿Aceptan mascotas en el establecimiento?

📈 Futuras Mejoras
[ ] Memoria conversacional por usuario (Chat History).

[ ] Persistencia de interacciones en base de datos PostgreSQL/MySQL.

[ ] Dashboard administrativo con Streamlit.

[ ] Integración con WhatsApp Business API.


👨‍💻 Autor
**Juan Carlos Palma Adones**

*Proyecto desarrollado como práctica de Inteligencia Artificial utilizando LangChain y RAG.*
