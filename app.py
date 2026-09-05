from dotenv import load_dotenv
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from langchain_groq import ChatGroq

from langchain_core.messages import SystemMessage, HumanMessage

from tools import get_weather, web_search, calculator, create_plan

# Load .env
load_dotenv()

# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# Bind tools to LLM
tools = [get_weather, web_search, calculator, create_plan]
llm_with_tools = llm.bind_tools(tools)

# ---------------- STATE ----------------

class AgentState(TypedDict):
    user_input: str
    response: str

# ---------------- NODE ----------------

def assistant_node(state: AgentState) -> AgentState:
    user_input = state["user_input"]

    print("\n[THINK] Understanding request...")
    messages = [
        SystemMessage(content="""
You are a helpful AI assistant.

Use tools ONLY for:
- weather information,
- web search,
- mathematical calculations,
- creating step-by-step plans when the user explicitly asks for a plan.

For health, education, coding, explanations, and general advice, answer directly without using tools.
"""),
        HumanMessage(content=user_input)
    ]

    result = llm_with_tools.invoke(messages)

    # If tool calls exist (be permissive about result shape)
    tool_calls = getattr(result, "tool_calls", None)
    if tool_calls:
        tool_call = tool_calls[0]

        # support dict-like or attribute-like tool_call
        if isinstance(tool_call, dict):
            tool_name = tool_call.get("name")
            tool_args = tool_call.get("args", {})
        else:
            tool_name = getattr(tool_call, "name", None)
            tool_args = getattr(tool_call, "args", {}) or {}

        print(f"[ACT] Calling tool: {tool_name}")

        tool_map = {
            "get_weather": get_weather,
            "web_search": web_search,
            "calculator": calculator,
            "create_plan": create_plan
        }

        tool_func = tool_map.get(tool_name)
        tool_result = None
        if tool_func is not None:
            # call either .invoke(...) or the function directly
            try:
                if hasattr(tool_func, "invoke"):
                    tool_result = tool_func.invoke(tool_args)
                else:
                    if isinstance(tool_args, dict):
                        tool_result = tool_func(**tool_args)
                    else:
                        tool_result = tool_func(tool_args)
            except TypeError:
                # fallback: try calling with the raw arg
                try:
                    tool_result = tool_func(tool_args)
                except Exception as e:
                    tool_result = f"Tool call failed: {e}"
        else:
            tool_result = f"Unknown tool: {tool_name}"

        print("[OBSERVE] Tool result received.")

        return {
            "user_input": user_input,
            "response": str(tool_result)
        }

    # Normal LLM response
    print("[OBSERVE] LLM response received.")

    content = getattr(result, "content", None)
    if content is None:
        # try common alternatives
        content = str(result)

    return {
        "user_input": user_input,
        "response": content
    }

# ---------------- GRAPH ----------------

graph = StateGraph(AgentState)

graph.add_node("assistant", assistant_node)

graph.add_edge(START, "assistant")
graph.add_edge("assistant", END)

app = graph.compile()

# ---------------- CHAT LOOP ----------------

print("🤖 LangGraph Smart AI Assistant")
print("Type 'exit' to quit")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    result = app.invoke({
        "user_input": user_input,
        "response": ""
    })

    print("\nAssistant:", result["response"])