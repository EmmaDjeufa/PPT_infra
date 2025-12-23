```markdown
# PPT_infra – Chatbot & Image Generator

A web app combining a GPT-powered chatbot with DALL·E image generation. Dockerized and cloud-ready.

**Live Demo:** [PPT_infra Web App](https://chatbot-dalle.onrender.com/)

---

## Project Structure

```

ppt_infra/
├─ app.py           # Flask backend
├─ dalle.py         # OpenAI DALL·E integration
├─ chat_llm.py      # OpenAI GPT integration
├─ requirements.txt # Python dependencies
├─ Dockerfile       # Containerization
├─ docker-compose.yml # Multi-container orchestration
├─ .env / .env.example # API keys
└─ Frontend/
├─ index.html    # Web interface
└─ main.js       # Frontend logic

````

---

## Local Deployment

### 1. Clone the Repository
```bash
git clone https://github.com/EmmaDjeufa/PPT_infra.git
cd PPT_infra
````

### 2. Configure Environment

```bash
cp .env.example .env
```

Add your GPT and DALL·E API keys in `.env`.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Locally

Without Docker:

```bash
python app.py
```

With Docker:

```bash
docker build -t ppt_infra .
docker-compose up
```

Access: [http://localhost:5000](http://localhost:5000)
Stop Docker: `docker-compose down`

---

## Features

* Flask backend with modular structure
* Responsive frontend for chat & image generation
* GPT & DALL·E integration
* Dockerized, cloud-ready
* API keys secured via `.env`

---

## Feedback & Contributions

* Open an [issue](https://github.com/EmmaDjeufa/PPT_infra/issues) for bugs or suggestions
* Fork & submit pull requests
* Contact via GitHub for inquiries

