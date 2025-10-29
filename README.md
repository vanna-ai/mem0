# Mem0 + Vanna AI (User Preference Memory Demo)

A minimal proof-of-concept showing how to integrate **Vanna AI** — a conversational analytics engine — with **Mem0**, a universal memory layer for AI agents, to demonstrate how persistent user memory can personalize data queries.

---

## ⚙️ Features

- 🧠 **Mem0 Integration** — Stores and retrieves user preferences or context across sessions  
- 🪄 **Vanna API** — Answers analytical questions using `/chat_sse` endpoint  
- 💬 **Interactive CLI** — Prompts the user to add or view stored preferences before asking a question  
- 🔐 **.env-based Config** — Secure, no hard-coded API keys  
- 🧩 **Local-First Setup** — Works directly from terminal without a frontend  

---

## 🚀 Setup

To get started:

1. Clone the repository  
   git clone https://github.com/vanna-ai/mem0.git  
   cd mem0  

2. Create and activate a virtual environment  
   python3 -m venv venv  
   source venv/bin/activate  

3. Install dependencies  
   pip install -r requirements.txt  

4. Copy the example environment file and fill in your keys  
   cp .env.example .env  

5. Run the script  
   python main.py  

---

## 💬 Example Flow

🤖 Checking what I already know about you...

🧠 Here are your current preferences:  
1. User requests that returned user data include days_since_signup and date_of_last_question  

Would you like to add any new preferences? (press Enter to skip)  
➡️  Your new preference: include organization name  
💾 Saved: "include organization name"

Now, what question would you like to ask?  
❓ Your question: hosted app usage for adi@vanna.ai  
📤 Sent to Vanna API...

---

## 🔑 Environment Variables (`.env.example`)

VANNA_API_KEY=  
VANNA_USER_EMAIL=  

MEM0_API_KEY=  
MEM0_USER_EMAIL=  
MEM0_ORG_ID=  
MEM0_PROJECT_ID=  

---

## 📁 Repository Structure

.
├── main.py  
├── test_mem0_sdk.py  
├── requirements.txt  
├── .env.example  
├── .gitignore  
└── README.md  

---

## 👨‍💻 Author

**Vanna AI**  
*Description:* Demo showcasing persistent memory with Mem0 to personalize Vanna analytics.  
🌐 [https://vanna.ai](https://vanna.ai)

---

## 🧠 About Vanna

[Vanna AI](https://vanna.ai) is a **conversational analytics engine** that connects to your databases and lets you ask business questions in natural language — returning SQL, charts, or dataframes as responses.

---

## 🧠 About Mem0

[Mem0](https://mem0.ai) is a **universal memory layer** for AI agents — enabling them to remember user preferences, context, and history across sessions. Perfect for personalization, state management, and long-term contextual reasoning.
