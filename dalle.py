#dalle.py
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
    print("Réponse OpenAI:", resp)

    # ---- 1. Cas erreur de quota / facturation ----
    if "error" in resp:
        err = resp["error"]

        if err.get("code") == "billing_hard_limit_reached":
            return {
                "error": True,
                "message": "Vos crédits OpenAI sont épuisés. Réactivez la facturation pour continuer à générer des images.",
                "billing_url": "https://platform.openai.com/account/billing"
            }

        # Autres erreurs API
        return {
            "error": True,
            "message": err.get("message", "Erreur inconnue.")
        }

    # ---- 2. Cas normal : image générée ----
    if "data" in resp:
        return {
            "error": False,
            "url": resp["data"][0]["url"]
        }

    # ---- 3. Cas inattendu ----
    return {
        "error": True,
        "message": "Réponse inattendue de l'API OpenAI."
    }
