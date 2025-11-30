import os
import requests

API_KEY = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    r = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"model": "gpt-image-1", "prompt": prompt, "size": "1024x1024"}
    )
    return r.json()["data"][0]["url"]