#chat_llm.py
import os
import requests

API_KEY = os.getenv("OPENAI_API_KEY")

def ask_chat(message):
    r = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": message}]
        }
    )
    return r.json()["choices"][0]["message"]["content"]