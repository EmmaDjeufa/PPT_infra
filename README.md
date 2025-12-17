
# PPT_infra – Chatbot & Générateur d’Images

**PPT_infra** est une application web intégrant un **chatbot intelligent** et un **générateur d’images via DALL·E**, démontrant mes compétences en **cloud computing, architecture scalable et développement full-stack**. Il est accessible à partir de ce lien : https://chatbot-dalle.onrender.com

## Structure du projet

```
ppt_infra/
├─ app.py           # Backend Flask : API pour chatbot et génération d’images
├─ dalle.py         # Intégration API OpenAI DALL·E
├─ chat_llm.py      # Intégration API OpenAI GPT
├─ requirements.txt # Dépendances Python
├─ Dockerfile       # Conteneurisation de l’application
├─ docker-compose.yml # Orchestration multi-conteneurs
├─ .env / .env.example # Configuration sécurisée
├─ README.md
├─ .gitignore
└─ Frontend
   ├─ index.html    # Interface web responsive
   └─ main.js       # Logique frontend (chat & génération d’images)
```

## Points clés

* **Backend robuste** : Flask avec gestion des erreurs et modularité pour faciliter la maintenance.
* **Frontend intuitif** : interface claire, responsive et centrée sur l’expérience utilisateur.
* **Cloud-ready & DevOps** : conteneurisation via Docker, orchestration avec Docker Compose, prêt pour un déploiement scalable sur tout environnement cloud.
* **Intégration d’API tierces** : OpenAI GPT pour le chatbot, DALL·E pour la génération d’images.
* **Sécurité et bonnes pratiques** : gestion des clés API via `.env`, séparation claire entre front et back.

## Objectif

Créer une **solution complète** démontrant mes compétences techniques en architecture cloud, conteneurisation et développement full-stack, tout en offrant une expérience utilisateur fluide et moderne.

