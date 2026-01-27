# chat_llm.py
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
        r.raise_for_status()  # déclenche HTTPError si code != 200
        return r.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        # Gestion spécifique pour 429
        if r.status_code == 429:
            return "⚠️ Trop de requêtes OpenAI. Veuillez réessayer dans quelques secondes."
        return f"Erreur serveur OpenAI : {e}"
    except requests.exceptions.RequestException as e:
        return f"Erreur serveur OpenAI : {e}"
