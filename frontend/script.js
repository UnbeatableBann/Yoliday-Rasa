const chatWindow = document.getElementById('chat-window');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

function appendMessage(text, sender = 'bot') {
  const msgDiv = document.createElement('div');
  msgDiv.className = `message ${sender}`;
  msgDiv.textContent = text;
  chatWindow.appendChild(msgDiv);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendMessage(message) {
  appendMessage(message, 'user');
  userInput.value = '';
  // Replace the URL below with your backend endpoint
  try {
    const response = await fetch('https://rasa-app-e7d2o.ondigitalocean.app/webhooks/rest/webhook', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sender: 'user', message })
    });
    const data = await response.json();
    if (data.length === 0) {
      appendMessage("Sorry, I didn't get that. Can you rephrase?", 'bot');
    } else {
      data.forEach(msg => {
        if (msg.text) appendMessage(msg.text, 'bot');
      });
    }
  } catch (err) {
    appendMessage('Error connecting to the assistant. Please try again later.', 'bot');
  }
}

chatForm.addEventListener('submit', function(e) {
  e.preventDefault();
  const message = userInput.value.trim();
  if (message) {
    sendMessage(message);
  }
});

userInput.addEventListener('keydown', function(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    chatForm.dispatchEvent(new Event('submit'));
  }
});
