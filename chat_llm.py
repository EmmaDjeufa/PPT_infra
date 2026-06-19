# chat_llm.py
import os
from google import genai

print("PPT_INFRA_KEY =", os.getenv("PPT_INFRA_KEY"))

client = genai.Client(
    api_key=os.getenv("PPT_INFRA_KEY")
)

def ask_chat(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )

        return response.text

    except Exception as e:
        return f"Erreur Gemini : {str(e)}"