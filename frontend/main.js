//main.js
// Récupération des éléments du DOM
const chatbox = document.getElementById("chatbox");
const imageBox = document.getElementById("imageBox");

// Base URL pour le backend
const BASE_URL = ""; // laisse vide si frontend et backend sont dans le même container

// Fonction pour ajouter un message dans le chat
function addMessage(text, sender) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message");

    const bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.textContent = text;

    if (sender === "user") {
        msgDiv.classList.add("user-message");  // aligné à droite
    } else {
        msgDiv.classList.add("bot-message");   // aligné à gauche
    }

    msgDiv.appendChild(bubble);
    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight; // scroll automatique
}

// Fonction pour envoyer un message au chatbot
async function sendMessage() {
    const msg = document.getElementById("msg").value;
    if (!msg) return;

    addMessage(msg, "user"); // afficher le message utilisateur
    document.getElementById("msg").value = "";

    try {
        const res = await fetch(`${BASE_URL}/chat`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: msg })
        });
        const data = await res.json();
        addMessage(data.reply, "bot"); // afficher la réponse du bot
    } catch (e) {
        addMessage(`Erreur: ${e}`, "bot");
    }
}
    function goHome() {
        window.location.href = "home.html";
    }

    function quitSite() {
        window.close();
        setTimeout(() => {
            window.location.href = "about:blank";
        }, 200);
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

        if (data.error) {
            // Message clair avec lien de réactivation
            imageBox.innerHTML = `
                ❌ <strong>La génération d'images est actuellement désactivée.</strong><br>
                Veuillez ajouter un moyen de paiement pour réactiver la fonctionnalité.<br><br>
                <a href="https://platform.openai.com/account/billing" target="_blank" style="color:blue;">
                    🔗 Réactiver la facturation OpenAI
                </a>
            `;
            return;
        }

        // Affichage normal de l'image si tout est ok
        imageBox.innerHTML = `<img src="${data.image_url}" alt="Image générée">`;
    } catch (e) {
        imageBox.innerHTML = `Erreur: ${e}`;
    }
}
