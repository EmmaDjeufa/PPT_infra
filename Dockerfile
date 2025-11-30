# Image Python officielle
FROM python:3.10-slim

# Dossier de travail
WORKDIR /app

# Copier le backend
COPY app.py /app/
COPY chat_llm.py /app/
COPY dalle.py /app/

# Copier le frontend
COPY frontend/ /app/frontend/

# Installer dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de Flask
EXPOSE 5000

# Commande de lancement
CMD ["python", "app.py"]