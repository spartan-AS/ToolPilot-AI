from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    data = {
        "Noida": "32°C, Sunny",
        "Delhi": "34°C, Hot",
        "Jaipur": "36°C, Dry"
    }
    return data.get(city, "Weather data not available")

@tool
def web_search(query: str) -> str:
    """Search the web for a query."""
    fake_db = {
        "langgraph": "LangGraph official documentation and GitHub repository",
        "python": "Python official documentation and Real Python tutorials"
    }
    return fake_db.get(query.lower(), "No results found")

@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

@tool
def create_plan(goal: str) -> str:
    """
Create a step-by-step action plan ONLY when the user explicitly asks for a plan, roadmap, schedule, study plan, project plan, or learning plan.
Do NOT use this tool for health advice, explanations, or general questions.
"""