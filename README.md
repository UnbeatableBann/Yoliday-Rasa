# 🌴 Yoliday Travel Assistant Bot — Rasa Internship Assessment

Welcome to the **Yoliday Travel Assistant Bot**, an intelligent chatbot built using the [Rasa](https://rasa.com) framework. This project was created as part of the Yoliday Rasa Bot Development Internship Assessment.

The assistant helps users with travel planning, weather updates, itinerary suggestions, and packing recommendations.

---

## 📦 Features

* Weather-based recommendations
* Smart packing suggestions
* Trip itinerary planning
* Natural, conversational experience using Rasa NLU + custom actions

---

## 🚀 Live Deployments

| Service          | Link                                                                           |
| ---------------- | ------------------------------------------------------------------------------ |
| Rasa Server   | [Rasa Render](https://yoliday-rasa.onrender.com)         |
| Frontend UI   | [Frontend Render](https://yoliday-rasa.onrender.com)                           |

---
## 🔌 Test Rasa Server with cURL

Use the following cURL command to send a message to the deployed Rasa server:

```bash
curl -X POST https://rasa-qor5.onrender.com/webhooks/rest/webhook \
     -H "Content-Type: application/json" \
     -d '{"sender": "test_user", "message": "Hi"}'
```

This will return the bot’s response from the Rasa server.

---

## 🐳 Docker Image Links

| Component          | Docker Image URL                                               |
| ------------------ | -------------------------------------------------------------- |
| Rasa with frontend | `docker.io/unbeatablebann/rasa`                                |

To pull and run the image:

```bash
docker pull yourusername/yoliday-rasa-backend
```

---

## ⚙️ Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/UnbeatableBann/Yoliday-Rasa.git
cd Yoliday-Rasa-Chatbot-backend
```

### 2. Create and Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Rasa Model

```bash
rasa train
```

### 5. Start the Action Server

```bash
rasa run actions
```

### 6. Start the Rasa Server

```bash
rasa run --enable-api --cors "*" --port 5005
```

---

## 🌐 Frontend Setup

### Deploy on Render

1. Go to [https://render.com](https://render.com) → **New → Static Site**.
2. Connect your GitHub repo and choose the frontend folder.
3. Set **Publish Directory** to `frontend`.
4. Done! Your frontend will be hosted like:
   [Yoliday Frontend](https://yoliday-rasa.onrender.com)

---

## 💬 Sample Conversation

```plaintext
User: Hi  
Bot: Hello! How can I help you with your travel plans today?

User: I want to check the weather in Mumbai  
Bot: Please wait while I fetch the weather for Mumbai...  
Bot: The current weather in Mumbai is 32°C, partly cloudy. You should pack light clothing and sunscreen!

User: What is Rasa?  
Bot: Rasa is an open-source machine learning framework for building AI assistants.

User: Bye  
Bot: Goodbye! Have a great trip!
```

---

## 📂 Project Structure

```
Yoliday-Rasa/
├── actions/                # Custom Python actions
├── data/                   # NLU training data
├── domain.yml              # Assistant's knowledge base
├── config.yml              # NLP pipeline and policies
├── models/                 # Trained models
├── frontend/               # Static HTML + JS chatbot UI
├── Dockerfile              # Docker build config
└── requirements.txt        # Python dependencies
└── start.sh                # Start command
```

---

## 📬 Contact / Credits

This bot was developed by **Shadab Jamadar** as part of the **Yoliday Rasa Internship Assessment**.
🔗 Connect on [LinkedIn](https://www.linkedin.com/in/shadab-jamadar-aa9b38252/)
💻 Explore more at [GitHub](https://github.com/UnbeatableBann)
