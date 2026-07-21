from dotenv import load_dotenv
import os

from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

print("Modelos disponibles:\n")

for model in client.models.list():
    print(model.name)