from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from chat_llm import ask_chat
from dalle import generate_image
import os


# IMPORTANT : pas de static_url_path=''
app = Flask(__name__, static_folder="frontend")
CORS(app)
# Autoriser toutes les origines pendant le développement
CORS(app, resources={r"/*": {"origins": "*"}})# Autoriser toutes les origines pendant le développement

# Frontend
@app.route("/")
def serve_frontend():
    return send_from_directory("frontend", "home.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    reply = ask_chat(message)
    return jsonify({"reply": reply})

# Image API
@app.route("/image", methods=["POST"])
def image():
    data = request.get_json()
    prompt = data.get("prompt", "")
    result = generate_image(prompt)
    return jsonify(result)

# Lancement
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
