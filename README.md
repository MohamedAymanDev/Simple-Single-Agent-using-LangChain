# 🤖 AI Research & Weather Agent

A simple **AI Agent** built with **LangChain** and **Google Gemini** that can reason about user requests and dynamically use external tools to find information and retrieve current weather data.

The project demonstrates how an LLM can work as an **agent**, decide which tool to use, execute it, and generate a final grounded response.

---

## 🚀 Features

* 🤖 AI Agent powered by **Google Gemini**
* 🔎 Real-time web search using **Tavily**
* 🌤️ Current weather information using **WeatherStack**
* 🧠 ReAct-based agent reasoning
* 🔧 Dynamic tool selection
* 💬 Interactive **Streamlit GUI**
* ✨ Animated futuristic UI
* ⚡ Error handling for agent parsing and API errors

---

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
              ┌───────────────┐
              │  Streamlit UI │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │  LangChain    │
              │     Agent     │
              └───────┬───────┘
                      │
             ┌────────┼────────┐
             ▼        ▼        ▼
         Gemini    Tavily   WeatherStack
           LLM      Search      API
             │        │        │
             └────────┼────────┘
                      ▼
                Final Answer
```

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Google Gemini**
* **Tavily Search**
* **WeatherStack API**
* **Streamlit**
* **Requests**
* **python-dotenv**

---

## 📂 Project Structure

```text
AI-Research-Weather-Agent/
│
├── main.py
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
WEATHERSTACK_API_KEY=your_weatherstack_api_key
```

> ⚠️ Never upload your `.env` file or expose your API keys on GitHub.

Add this to `.gitignore`:

```text
.env
.venv/
__pycache__/
```

---

## 📦 Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd AI-Research-Weather-Agent
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

The agent can reason about the request and use the available tools to retrieve the required information.

Example workflow:

```text
User Question
      ↓
Gemini analyzes the request
      ↓
Select appropriate tool
      ↓
Tavily Search / WeatherStack
      ↓
Gemini processes the result
      ↓
Final Answer
```

---

## 🧠 What I Learned

Through this project, I practiced:

* Building AI Agents with LangChain
* Understanding the **ReAct Agent** pattern
* Connecting LLMs with external tools
* Tool calling and dynamic tool selection
* Working with REST APIs
* Managing API keys using environment variables
* Building interactive AI applications with Streamlit
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
* Deploy the application online

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
