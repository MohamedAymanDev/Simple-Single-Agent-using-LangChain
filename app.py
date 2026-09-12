import streamlit as st
import time
from main import agent_executor


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

/* Background */

.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(99,102,241,0.18), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(168,85,247,0.15), transparent 30%),
        radial-gradient(circle at 50% 100%, rgba(59,130,246,0.12), transparent 35%),
        #020617;
}

/* Remove top spacing */

.block-container {
    padding-top: 2rem;
    max-width: 1400px;
}


/* =========================================================
   ANIMATED ORB
   ========================================================= */

.orb-container {
    display: flex;
    justify-content: center;
    margin-top: 10px;
    margin-bottom: 20px;
}

.orb {
    width: 100px;
    height: 100px;
    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 45px;

    background:
        radial-gradient(circle at 30% 30%,
        #ffffff,
        #a78bfa 15%,
        #6366f1 40%,
        #312e81 75%);

    box-shadow:
        0 0 20px #6366f1,
        0 0 50px rgba(99,102,241,0.6),
        0 0 100px rgba(139,92,246,0.4);

    animation:
        float 3s ease-in-out infinite,
        glow 2s ease-in-out infinite alternate;
}

@keyframes float {

    0%, 100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-12px);
    }

}

@keyframes glow {

    from {
        box-shadow:
            0 0 20px #6366f1,
            0 0 50px rgba(99,102,241,0.5);
    }

    to {
        box-shadow:
            0 0 35px #8b5cf6,
            0 0 90px rgba(139,92,246,0.8);
    }

}


/* =========================================================
   HERO
   ========================================================= */

.hero {
    text-align: center;
    margin-bottom: 35px;
}

.hero-title {

    font-size: 46px;
    font-weight: 800;

    background:
        linear-gradient(
            90deg,
            #818cf8,
            #c084fc,
            #60a5fa,
            #818cf8
        );

    background-size: 300%;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: gradientMove 6s ease infinite;
}

@keyframes gradientMove {

    0% {
        background-position: 0%;
    }

    50% {
        background-position: 100%;
    }

    100% {
        background-position: 0%;
    }

}

.hero-subtitle {
    color: #94a3b8;
    font-size: 17px;
    margin-top: 8px;
}


/* =========================================================
   STATUS
   ========================================================= */

.status {

    display: inline-flex;

    align-items: center;

    gap: 8px;

    padding: 7px 15px;

    border-radius: 30px;

    background: rgba(34,197,94,0.10);

    border: 1px solid rgba(34,197,94,0.25);

    color: #86efac;

    font-size: 13px;

    margin-top: 15px;

}

.status-dot {

    width: 8px;
    height: 8px;

    border-radius: 50%;

    background: #22c55e;

    box-shadow: 0 0 12px #22c55e;

    animation: pulse 1.5s infinite;

}

@keyframes pulse {

    0%,100% {
        opacity: 1;
        transform: scale(1);
    }

    50% {
        opacity: 0.4;
        transform: scale(1.4);
    }

}


/* =========================================================
   TOOL CARDS
   ========================================================= */

.tool-card {

    background:
        linear-gradient(
            145deg,
            rgba(30,41,59,0.75),
            rgba(15,23,42,0.55)
        );

    border: 1px solid rgba(148,163,184,0.12);

    border-radius: 20px;

    padding: 22px;

    backdrop-filter: blur(18px);

    transition:
        transform 0.3s ease,
        border-color 0.3s ease,
        box-shadow 0.3s ease;

    height: 150px;
}

.tool-card:hover {

    transform: translateY(-7px);

    border-color: rgba(129,140,248,0.45);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.3),
        0 0 25px rgba(99,102,241,0.15);

}

.tool-icon {

    font-size: 30px;

    margin-bottom: 10px;
}

.tool-title {

    color: #f8fafc;

    font-size: 17px;

    font-weight: 700;

}

.tool-desc {

    color: #94a3b8;

    font-size: 13px;

    margin-top: 5px;

}


/* =========================================================
   GLASS PANEL
   ========================================================= */

.glass-panel {

    background: rgba(15,23,42,0.62);

    border:
        1px solid rgba(148,163,184,0.10);

    border-radius: 24px;

    padding: 28px;

    backdrop-filter: blur(20px);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.25);

}


/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #020617,
            #0f172a
        );

    border-right:
        1px solid rgba(148,163,184,0.1);

}

.sidebar-title {

    font-size: 24px;

    font-weight: 800;

    color: #f8fafc;

}

.sidebar-text {

    color: #94a3b8;

    font-size: 13px;

}


/* =========================================================
   INPUT
   ========================================================= */

.stTextInput input {

    background: rgba(15,23,42,0.8) !important;

    border:
        1px solid rgba(129,140,248,0.25) !important;

    border-radius: 15px !important;

    color: white !important;

    padding: 15px !important;

}

.stTextInput input:focus {

    border-color: #818cf8 !important;

    box-shadow:
        0 0 20px rgba(99,102,241,0.2) !important;

}


/* =========================================================
   BUTTON
   ========================================================= */

.stButton button {

    border-radius: 14px !important;

    border: 1px solid rgba(129,140,248,0.25) !important;

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        ) !important;

    color: white !important;

    font-weight: 700 !important;

    transition: all 0.25s ease !important;

}

.stButton button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 10px 30px rgba(99,102,241,0.35);

}


/* =========================================================
   RESPONSE
   ========================================================= */

.response-box {

    margin-top: 25px;

    background:
        linear-gradient(
            145deg,
            rgba(30,41,59,0.8),
            rgba(15,23,42,0.65)
        );

    border-radius: 20px;

    padding: 25px;

    border:
        1px solid rgba(129,140,248,0.15);

    color: #e2e8f0;

    line-height: 1.7;

}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {

    text-align: center;

    margin-top: 50px;

    color: #475569;

    font-size: 12px;

}

</style>
""")


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.html("""
    <div class="sidebar-title">
        🤖 AI Agent
    </div>

    <div class="sidebar-text">
        Intelligent research & weather assistant
    </div>
    """)

    st.divider()

    st.markdown("### ⚙️ Agent Stack")

    st.success("🟢 Gemini LLM")
    st.info("🔎 Tavily Search")
    st.warning("🌤️ WeatherStack")

    st.divider()

    st.markdown("### 🧠 Capabilities")

    st.markdown("""
    - 🔎 Web Research
    - 🌤️ Weather Data
    - 🤖 Reasoning
    - 🔧 Tool Calling
    - 🧩 Multi-step Tasks
    """)

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# =========================================================
# HEADER
# =========================================================

st.html("""
<div class="orb-container">

    <div class="orb">
        🤖
    </div>

</div>

<div class="hero">

    <div class="hero-title">
        AI Research Agent
    </div>

    <div class="hero-subtitle">
        Search the web • Analyze information • Get live weather
    </div>

    <div class="status">

        <span class="status-dot"></span>

        Agent Online

    </div>

</div>
""")


# =========================================================
# TOOLS SECTION
# =========================================================

st.markdown("### 🧩 Agent Tools")

col1, col2, col3 = st.columns(3)

with col1:

    st.html("""
    <div class="tool-card">

        <div class="tool-icon">
            🧠
        </div>

        <div class="tool-title">
            Gemini
        </div>

        <div class="tool-desc">
            Reasoning & natural language generation
        </div>

    </div>
    """)


with col2:

    st.html("""
    <div class="tool-card">

        <div class="tool-icon">
            🔎
        </div>

        <div class="tool-title">
            Tavily Search
        </div>

        <div class="tool-desc">
            Real-time web research
        </div>

    </div>
    """)


with col3:

    st.html("""
    <div class="tool-card">

        <div class="tool-icon">
            🌤️
        </div>

        <div class="tool-title">
            WeatherStack
        </div>

        <div class="tool-desc">
            Current weather information
        </div>

    </div>
    """)


st.write("")


# =========================================================
# CHAT STATE
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# =========================================================
# EXAMPLES
# =========================================================

st.markdown("### 💡 Try an example")

example_col1, example_col2, example_col3 = st.columns(3)

example1 = example_col1.button(
    "🇪🇬 Egypt + Weather",
    use_container_width=True
)

example2 = example_col2.button(
    "🌍 Search + Weather",
    use_container_width=True
)

example3 = example_col3.button(
    "🔎 Web Research",
    use_container_width=True
)


if example1:

    st.session_state.example_prompt = (
        "Find the capital of Egypt and then find its current weather"
    )

elif example2:

    st.session_state.example_prompt = (
        "Find the capital of France and then find its current weather"
    )

elif example3:

    st.session_state.example_prompt = (
        "What are the latest developments in generative AI?"
    )


# =========================================================
# CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =========================================================
# INPUT
# =========================================================

default_prompt = st.session_state.pop(
    "example_prompt",
    ""
)

prompt = st.chat_input(
    "Ask the AI Agent anything..."
)


if default_prompt and not prompt:

    prompt = default_prompt


# =========================================================
# RUN AGENT
# =========================================================

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)


    with st.chat_message("assistant"):

        with st.status(
            "🤖 Agent is thinking...",
            expanded=True
        ):

            st.write("🧠 Analyzing your request...")
            time.sleep(0.5)

            st.write("🔧 Selecting the best tool...")
            time.sleep(0.5)

            st.write("⚡ Executing agent...")
            
            try:

                response = agent_executor.invoke(
                    {
                        "input": prompt
                    }
                )

                answer = response["output"]

                st.write("✅ Task completed")

            except Exception as e:

                answer = f"❌ Error: {str(e)}"


        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">

    Built with ❤️ using
    LangChain • Gemini • Tavily • WeatherStack • Streamlit

</div>
""")