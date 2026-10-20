
<div align="center">

# 📝 TaskFlow AI

### ✨ From Messy Thoughts to an Organized Day

<p>
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=8B5CF6&center=true&vCenter=true&width=650&lines=Write+Naturally+%F0%9F%92%AC;Extract+Tasks+with+AI+%F0%9F%A4%96;Prioritize+What+Matters+%E2%9C%A8;Plan+Your+Day+Smarter+%F0%9F%93%85" alt="Animated TaskFlow AI typing banner" />
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/LangGraph-Workflow-7C3AED?style=for-the-badge" alt="LangGraph" />
  <img src="https://img.shields.io/badge/Groq-AI%20Inference-F55036?style=for-the-badge" alt="Groq" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
</p>

**An AI-powered task organizer that transforms everyday language into a clear, prioritized to-do list.**

</div>

---

## 🌟 Overview

Ever feel like your mind is full of tasks, deadlines, and plans?

TaskFlow AI helps turn those thoughts into an organized action list. Simply describe what you need to do in natural language, and the AI extracts individual tasks, assigns priorities, and displays the results in a clean web interface.

### 💬 Example input

> I need to finish my assignment tomorrow, buy groceries today, and prepare for my meeting next week.

### ⚡ What TaskFlow AI does

- 🧠 Extracts individual tasks from natural-language input
- 🔥 Assigns **High**, **Medium**, or **Low** priorities
- 📋 Organizes tasks into a readable list
- 🔄 Uses LangGraph to manage the AI workflow
- 🖥️ Provides a simple interface powered by Streamlit

---

## 🎬 How It Works

```mermaid
flowchart TD
    A(["💬 Natural Language Input"]) --> B["🧠 Node 1: Task Extraction"]
    B --> C["🎯 Node 2: Task Prioritization"]
    C --> D["📋 Node 3: Format Results"]
    D --> E(["✅ Organized To-Do List"])

    style A fill:#ede9fe,stroke:#7c3aed,color:#312e81
    style B fill:#dbeafe,stroke:#2563eb,color:#1e3a8a
    style C fill:#fef3c7,stroke:#d97706,color:#78350f
    style D fill:#fce7f3,stroke:#db2777,color:#831843
    style E fill:#dcfce7,stroke:#16a34a,color:#14532d
```

### 🔹 Node 1 — Task Extraction
Groq AI identifies individual tasks from the user's message.

### 🔹 Node 2 — Task Prioritization
The AI assigns a priority based on urgency, importance, and any deadlines mentioned.

### 🔹 Node 3 — Format Results
The workflow formats tasks into a clear list, placing higher-priority tasks first.

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 Natural-language input | Describe tasks in your own words |
| 🧠 AI task extraction | Convert one message into separate tasks |
| 🔴 Priority labels | Identify High, Medium, and Low priorities |
| 📊 Smart organization | Sort tasks by priority |
| 🔗 LangGraph workflow | Run each processing step in sequence |
| 🖥️ Interactive interface | Enter tasks through a Streamlit web app |

---

## 🛠️ Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-Language-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Groq-LLM%20API-F55036?style=flat-square" alt="Groq" />
  <img src="https://img.shields.io/badge/LangChain-Integration-1C3C3C?style=flat-square" alt="LangChain" />
  <img src="https://img.shields.io/badge/LangGraph-Orchestration-7C3AED?style=flat-square" alt="LangGraph" />
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit" />
</p>

- **Python** — core application logic
- **Groq API** — language model inference
- **LangChain Groq** — integration with the Groq model
- **LangGraph** — multi-step workflow orchestration
- **Streamlit** — web application interface
- **python-dotenv** — environment variable management

---

## 📁 Project Structure

```text
TaskFlowAI/
│
├── src/
│   ├── __init__.py
│   ├── state.py
│   ├── agents.py
│   └── graph.py
│
├── static/
│
├── app.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

Follow these steps to run TaskFlow AI locally.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/TaskFlowAI.git
cd TaskFlowAI
```

Replace `YOUR_USERNAME` with your GitHub username after creating your repository.

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 3️⃣ Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Configure your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

> 🔐 Security: Never commit your `.env` file or expose your API key in screenshots, source code, or public repositories.

### 5️⃣ Launch the application

```bash
streamlit run app.py
```

Your browser should open the local TaskFlow AI web application.

---

## 🧪 Example Output

**Input:**

```text
I need to submit my assignment tomorrow,
clean my room this weekend,
and read a book when I have free time.
```

**Illustrative output:**

| Priority | Task |
|---|---|
| 🔴 High | Submit my assignment tomorrow |
| 🟡 Medium | Clean my room this weekend |
| 🟢 Low | Read a book in my free time |

*Example priorities are illustrative; actual AI classifications may differ.*

---

## 🔐 Responsible AI & Limitations

- AI-generated priorities may not always reflect the user's actual preferences.
- Review task labels and explanations before relying on them.
- The application does not automatically schedule reminders or calendar events.
- Model availability and API limits depend on the Groq account.
- Never place API credentials in public repositories.

---

## 🔮 Future Improvements

- [ ] Mark tasks as completed
- [ ] Allow users to edit AI-assigned priorities
- [ ] Add task categories and filters
- [ ] Save tasks between sessions
- [ ] Add due-date and reminder support
- [ ] Export the to-do list to CSV
- [ ] Add a task history dashboard

---

## 👩‍💻 Author

**Nargis Nizam**

AI & Data Science Student | Python Developer

<p>
  <a href="https://github.com/NargisNizam">
    <img src="https://img.shields.io/badge/GitHub-NargisNizam-181717?style=for-the-badge&logo=github" alt="GitHub Profile" />
  </a>
</p>

---

<div align="center">

### 💜 Plan Better. Prioritize Smarter. Get Things Done.

*Built with Python, Groq AI, and LangGraph.*

</div>
