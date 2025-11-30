from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from chat_llm import ask_chat    # Fonctions séparées dans d'autres fichiers
from dalle import generate_image

import os

app = Flask(__name__, static_folder="frontend", static_url_path="/")
CORS(app)   # Autorise les appels du frontend (Codespaces utilise des domaines séparés)


# ---------------------------
# ROUTE FRONTEND (index.html)
# ---------------------------

@app.route("/")
def serve_frontend():
    """
    Sert le fichier index.html situé dans /frontend/
    """
    return send_from_directory("frontend", "index.html")


# ---------------------------
# ROUTE CHATBOT
# ---------------------------

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint appelé par main.js pour envoyer une question et recevoir la réponse LLM.
    """
    data = request.get_json()
    message = data.get("message", "")

    reply = ask_chatbot(message)
    return jsonify({"reply": reply})


# ---------------------------
# ROUTE DALL·E
# ---------------------------

@app.route("/image", methods=["POST"])
def image():
    """
    Endpoint de génération d'image.
    """
    data = request.get_json()
    prompt = data.get("prompt", "")

    url = generate_image(prompt)
    return jsonify({"image_url": url})


# ---------------------------
# LANCEMENT LOCAL
# ---------------------------

if __name__ == "__main__":
    # Flask doit écouter sur 0.0.0.0 pour être visible depuis Codespaces
    app.run(host="0.0.0.0", port=5000, debug=True)