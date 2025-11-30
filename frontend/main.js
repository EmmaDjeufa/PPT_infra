// Récupération des éléments du DOM
const chatbox = document.getElementById("chatbox");
const imageBox = document.getElementById("imageBox");

// Base URL pour le backend : si tu changes de port ou Codespaces, modifie ici
//const BASE_URL = "https://didactic-space-winner-7559qvv9px53rqjr-5000.app.github.dev"; // vide si frontend et backend dans le même container, sinon mettre l'URL complète
const BASE_URL = "";
// Fonction pour envoyer un message au chatbot
async function sendMessage() {
    const msg = document.getElementById("msg").value;
    if (!msg) return;

    chatbox.innerHTML += `<div class="user">Vous: ${msg}</div>`;
    document.getElementById("msg").value = "";

    try {
        const res = await fetch(`${BASE_URL}/chat`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: msg })
        });
        const data = await res.json();
        chatbox.innerHTML += `<div class="bot">Bot: ${data.reply}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
    } catch (e) {
        chatbox.innerHTML += `<div class="bot">Erreur: ${e}</div>`;
    }
}

// Fonction pour générer une image avec DALL·E
async function generateImage() {
    const prompt = document.getElementById("prompt").value;
    if (!prompt) return;

    imageBox.innerHTML = "Génération en cours...";

    try {
        const res = await fetch(`${BASE_URL}/image`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt })
        });
        const data = await res.json();
        imageBox.innerHTML = `<img src="${data.image_url}" alt="Image générée">`;
    } catch (e) {
        imageBox.innerHTML = `Erreur: ${e}`;
    }
}