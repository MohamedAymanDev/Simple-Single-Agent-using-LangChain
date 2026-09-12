# 🤖 AI Research & Weather Agent

A simple **AI Agent** built with **LangChain** and **Groq** that can reason about user requests, dynamically select external tools, retrieve information, and provide current weather data.

The project demonstrates how an LLM can work as an **AI Agent**, understand a user's request, decide which tool is needed, execute it, process the results, and generate a final response.

## 🚀 Live Demo

👉 **Try the AI Agent:**
https://simple-single-agent-using-langchain-cbsscz6nfdpw4jcep55zpt.streamlit.app/

---

## 🚀 Features

* 🤖 AI Agent powered by **Groq**
* 🧠 **GPT-OSS-20B** as the LLM
* 🔎 Real-time web search using **Tavily**
* 🌤️ Current weather information using **WeatherStack**
* 🔧 Tool Calling and dynamic tool selection
* 🧩 LangChain Agent architecture
* 💬 Interactive **Streamlit GUI**
* ✨ Animated futuristic UI
* ⚡ Error handling for agent parsing and API errors

---

## 🏗️ Architecture

```text
                         User
                           │
                           ▼
                  ┌────────────────┐
                  │  Streamlit UI  │
                  └───────┬────────┘
                          │
                          ▼
                  ┌────────────────┐
                  │    LangChain   │
                  │      Agent     │
                  └───────┬────────┘
                          │
                 ┌────────┴────────┐
                 │                 │
                 ▼                 ▼
          ┌─────────────┐   ┌───────────────┐
          │    Groq     │   │     Tools     │
          │ GPT-OSS-20B │   │               │
          └─────────────┘   └───────┬───────┘
                                    │
                         ┌──────────┴──────────┐
                         ▼                     ▼
                  ┌────────────┐       ┌──────────────┐
                  │   Tavily   │       │ WeatherStack │
                  │   Search   │       │     API      │
                  └────────────┘       └──────────────┘
                         │                     │
                         └──────────┬──────────┘
                                    ▼
                              Final Answer
```

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Groq**
* **GPT-OSS-20B**
* **Tavily Search**
* **WeatherStack API**
* **Streamlit**
* **Requests**
* **python-dotenv**

---

## 📂 Project Structure

```text
Simple-Single-Agent-using-LangChain/
│
├── main.py
├── app.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
WEATHERSTACK_API_KEY=your_weatherstack_api_key
```


Add this to `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/MohamedAymanDev/Simple-Single-Agent-using-LangChain.git
cd Simple-Single-Agent-using-LangChain
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Agent

To run the agent from the terminal:

```bash
python main.py
```

To launch the Streamlit interface:

```bash
python -m streamlit run app.py
```

---

## 💡 Example

You can ask:

```text
Find the capital of Egypt and then find its current weather.
```

The agent understands the request, determines which tools are required, executes them, and combines the results into a final response.

### Example Workflow

```text
User Question
      ↓
GPT-OSS-20B analyzes the request
      ↓
Agent selects the appropriate tool
      ↓
Tavily Search / WeatherStack
      ↓
Tool returns the result
      ↓
GPT-OSS-20B processes the result
      ↓
Final Answer
```

---

## 🧠 What I Learned

Through this project, I practiced:

* Building AI Agents with **LangChain**
* Understanding **Tool Calling**
* Connecting LLMs with external tools
* Dynamic tool selection
* Working with REST APIs
* Integrating **Groq** with LangChain
* Using **GPT-OSS-20B** for agent-based applications
* Managing API keys using environment variables
* Building interactive AI applications with **Streamlit**
* Handling API and agent errors
* Creating a user-friendly AI application interface

---

## 🔮 Future Improvements

* Add more tools
* Add conversation memory
* Add RAG capabilities
* Add better agent observability
* Add response streaming
* Add tool execution history
* Add authentication
* Improve UI/UX
* Expand the agent with additional capabilities

---

## 👨‍💻 Author

**Mohamed Ayman Yahya Abdel Salam**

Aspiring Machine Learning Engineer | AI Student

Interested in:

* Machine Learning
* Deep Learning
* NLP
* Generative AI
* RAG
* AI Agents

---

⭐ If you find this project useful, feel free to star the repository!
