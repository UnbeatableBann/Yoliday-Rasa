# Yoliday Travel Assistant Bot - Rasa Internship Assessment

Welcome to the Yoliday Travel Assistant Bot! This project was built using the Rasa framework as part of the Yoliday Rasa Bot Development Internship Assessment.

---

## Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/UnbeatableBann/Yoliday-Rasa-Chatbot-backend.git
cd Yoliday-Rasa-Chatbot-backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Rasa Model

```bash
rasa train
```

### 5. Start Rasa Action Server

```bash
rasa run actions
```

### 6. Start Rasa Server

```bash
rasa run --enable-api --cors "*" --port $PORT
```

### 7. Start the Frontend

Open the `frontend/index.html` file in your browser or deploy it on Render.

---

## 💬 Sample Conversation

```
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

## Deployed Version

* **Rasa Server**: [https://yoliday-rasa-bot.onrender.com](https://yoliday-rasa.onrender.com)
* **Action Server**: [https://yoliday-action-server.onrender.com](https://yoliday-actions.onrender.com)
* **Frontend Chat UI**: [https://yoliday-frontend.onrender.com](https://yoliday-frontend.onrender.com)

Feel free to try out the bot and explore its features!
