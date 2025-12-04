"""import os
import requests

API_KEY = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    r = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"model": "gpt-image-1", "prompt": prompt, "size": "1024x1024"}
    )
    return r.json()["data"][0]["url"]"""

import os
import requests

API_KEY = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    r = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-image-1",
            "prompt": prompt,
            "size": "1024x1024"
        }
    )

    resp = r.json()
    print("Réponse OpenAI:", resp)  # <-- ajoute ça pour debug

    if "data" not in resp:
        raise Exception(f"Erreur API: {resp}"
    )

    if "error" in resp:
        if resp["error"]["code"] == "billing_hard_limit_reached":
        # On renvoie une erreur très claire
           raise Exception("Crédits OpenAI épuisés. Ajoutez un moyen de paiement pour utiliser la génération d'images."
    )


    return resp["data"][0]["url"]

