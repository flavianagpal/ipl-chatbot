# 🏏 IPL Chatbot with Persistent Memory

An AI-powered IPL chatbot built using **Python**, **Groq API**, and **MongoDB**. The chatbot can answer cricket-related questions, maintain conversational context, and remember previous conversations using persistent memory.

---

## 🚀 Features

- 🤖 AI-powered IPL chatbot using Groq LLM
- 💬 Natural, human-like conversations
- 🧠 Persistent conversational memory using MongoDB
- 📝 Custom system prompt for consistent chatbot behavior
- 🔐 Secure API key management using `.env`
- ⚡ Fast responses powered by Groq
- 📂 Conversation history stored by Thread ID

---

## 🛠️ Tech Stack

- Python
- Groq API
- MongoDB Atlas
- PyMongo
- python-dotenv
- Git & GitHub

---

## 📁 Project Structure

```
ipl-chatbot/
│── chatbot.py
│── test_mongo.py
│── .env
│── .gitignore
│── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/flavianagpal/ipl-chatbot.git
```

Move into the project folder.

```bash
cd ipl-chatbot
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create a `.env` file

Add the following:

```env
GROQ_API_KEY=your_groq_api_key

MONGODB_URI=your_mongodb_connection_string
```

---

### 4. Run the chatbot

```bash
python chatbot.py
```

---

## 💡 How It Works

1. User enters a message.
2. Previous conversation history is loaded from MongoDB.
3. The complete conversation is sent to the Groq LLM.
4. The model generates a response.
5. Both the user message and AI response are stored in MongoDB.
6. The chatbot remembers the conversation even after restarting the program.

---

## 🧠 Conversational Memory

Instead of storing messages only in a Python list, this project stores conversations in MongoDB.

Each conversation is identified using a **Thread ID**.

Example document stored in MongoDB:

```json
{
  "thread_id": "chat_1",
  "role": "user",
  "content": "My name is Flavia"
}
```

When the chatbot starts, it retrieves all previous messages associated with the Thread ID and continues the conversation seamlessly.

---

## 🎯 Prompt Engineering

The chatbot uses a carefully designed system prompt that defines:

- Personality
- Conversation style
- IPL expertise
- Communication guidelines
- Memory awareness
- Factual accuracy
- Response quality

This helps produce more natural, engaging, and consistent responses.

---

## 📸 Example Conversation

```
You: My name is Flavia.

Bot:
Nice to meet you, Flavia! I'll remember your name during this conversation.

You: What is my name?

Bot:
Your name is Flavia. You mentioned it earlier in our conversation.
```

---

## 🔮 Future Improvements

- Streamlit web interface
- Multiple chat threads
- User authentication
- Live IPL data integration
- Cricket API support
- Fantasy cricket recommendations
- RAG using IPL documents
- Conversation summarization
- Voice-based interaction

---

## 📌 Learning Outcomes

Through this project, I learned:

- Working with Large Language Models (LLMs)
- Prompt engineering
- API integration
- Environment variable management
- MongoDB integration with Python
- Persistent conversational memory
- Git and GitHub workflow
- Building conversational AI applications

---

