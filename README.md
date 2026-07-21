# ☕ Café Delicias del Norte - Agente IA con LangChain

Un chatbot inteligente desarrollado en Python utilizando **LangChain**, **Cohere**, **FAISS** y **Telegram**, capaz de responder preguntas sobre una cafetería utilizando la técnica **RAG (Retrieval-Augmented Generation)**.

---

## 🚀 Características

- 📄 Consulta información desde un documento PDF.
- 📊 Consulta productos y precios desde un archivo Excel.
- 🤖 Responde preguntas utilizando un LLM (Cohere).
- 🧠 Implementa RAG con FAISS para búsqueda semántica.
- 💬 Integración con Telegram.
- ⚡ Arquitectura modular y escalable.

---

## 🏗️ Arquitectura

```
Usuario
   │
   ▼
Telegram
   │
   ▼
Agente IA (LangChain)
   │
   ├───────────────┐
   ▼               ▼
FAISS          Productos Excel
   │
   ▼
Información PDF
```

---

## 📂 Estructura del proyecto

```
cafe-delicias-ai/
│
├── documentos/
│   ├── cafeteria.pdf
│   └── productos.xlsx
│
├── data/
│   └── faiss_index/
│
├── src/
│   ├── agent.py
│   ├── config.py
│   ├── excel_loader.py
│   ├── load_pdf.py
│   ├── rag.py
│   └── vectorstore.py
│
├── main.py
├── main_telegram.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Tecnologías utilizadas

- Python 3.13
- LangChain
- Cohere
- FAISS
- Pandas
- PyPDF
- Telegram Bot API

---

## ⚙️ Instalación

Crear un entorno virtual

```bash
python -m venv venv
```

Activar el entorno

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🔑 Variables de entorno

Crear un archivo `.env`

```text
COHERE_API_KEY=tu_api_key

TELEGRAM_TOKEN=tu_token
```

---

## ▶️ Ejecutar desde consola

```bash
python main.py
```

---

## 🤖 Ejecutar el bot de Telegram

```bash
python main_telegram.py
```

---

## 💬 Ejemplos de preguntas

- ¿Cuál es el horario de atención?
- ¿Aceptan tarjetas?
- ¿Cuánto cuesta un Café Latte?
- ¿Cuál es el sueldo de un cocinero?
- ¿Tienen WiFi?
- ¿Puedo llevar mascotas?
- ¿Cuánto cuesta una Chorrillana?

---

## 📈 Futuras mejoras

- Memoria conversacional.
- Historial de conversaciones.
- Base de datos SQL.
- Panel web con Streamlit.
- Agentes especializados.
- Integración con WhatsApp.
- Despliegue en Railway.

---

## 👨‍💻 Autor

Juan Carlos Palma Adones

Proyecto desarrollado como práctica de Inteligencia Artificial utilizando LangChain.