# =========================
# IMPORT LIBRARIES
# =========================

import os
import requests
import certifi

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.tools.tavily_search import TavilySearchResults
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain import hub


# =========================
# LOAD ENV VARIABLES
# =========================

os.environ["SSL_CERT_FILE"] = certifi.where()

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")


# =========================
# SEARCH TOOL
# =========================

search_tool = TavilySearchResults(
    max_results=2
)


# =========================
# WEATHER TOOL
# =========================

@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather information for a city.
    """

    url = (
        f"https://api.weatherstack.com/current?"
        f"access_key={WEATHERSTACK_API_KEY}"
        f"&query={city}"
    )

    response = requests.get(url)

    data = response.json()

    if "current" not in data:
        return f"Could not fetch weather data for {city}"

    return (
        f"City: {city}\n"
        f"Temperature: {data['current']['temperature']}°C\n"
        f"Weather: {data['current']['weather_descriptions'][0]}\n"
        f"Humidity: {data['current']['humidity']}%"
    )


# =========================
# LLM
# =========================

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


# =========================
# PROMPT
# =========================

prompt = hub.pull("hwchase17/openai-functions-agent")


# =========================
# TOOLS
# =========================

tools = [
    search_tool,
    get_weather_data
]


# =========================
# CREATE AGENT
# =========================

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)


# =========================
# AGENT EXECUTOR
# =========================

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)


# =========================
# TEST
# =========================

if __name__ == "__main__":

    response = agent_executor.invoke(
        {
            "input": (
                "Find the capital of Egypt "
                "and then find its current weather."
            )
        }
    )

    print("\n========================")
    print("FINAL OUTPUT")
    print("========================\n")

    print(response["output"])