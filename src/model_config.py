# Google Gemini
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch

# Load .env variables
load_dotenv()

# Read API keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# Initialize Gemini model
model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# Tavily tool
web_search = TavilySearch(max_results=5)
tools = [web_search]
