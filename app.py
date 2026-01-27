#app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from chat_llm import ask_chat
from dalle import generate_image
import os

app = Flask(__name__, static_folder="frontend")
CORS(app, resources={r"/*": {"origins": "*"}})

# ---------------------------
# API Chat
# ---------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    reply = ask_chat(message)
    return jsonify({"reply": reply})

# ---------------------------
# API Image
# ---------------------------
@app.route("/image", methods=["POST"])
def image():
    data = request.get_json()
    prompt = data.get("prompt", "")
    result = generate_image(prompt)
    return jsonify(result)

# ---------------------------
# Catch-all pour les fichiers statiques
# ---------------------------
@app.route("/", defaults={"path": "home.html"})
@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory(app.static_folder, path)

# ---------------------------
# Lancement
# ---------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
