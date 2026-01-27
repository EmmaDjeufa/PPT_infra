# chat_llm.py
import os
import requests

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY non défini !")

def ask_chat(message):
    try:
        r = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": message}]
            },
            timeout=15
        )
        r.raise_for_status()  # lève une exception si code != 200
        return r.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        # Retourne une erreur propre côté front
        return f"Erreur serveur OpenAI : {e}"
