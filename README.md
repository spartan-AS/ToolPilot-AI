# 🤖 ToolPilot AI — LangGraph Tool-Using AI Assistant

> **Ask naturally. Let the agent decide which tool to use.**

ToolPilot AI is a lightweight **LangGraph-based AI assistant** powered by **Groq Llama**, designed to intelligently route user queries through specialized tools.

Instead of using external tools for every request, the assistant first understands the user's query and determines whether it can answer directly or whether a specific tool is required.

The system currently supports tools for:

* 🌤️ **Weather**
* 🔎 **Web Search**
* 🧮 **Mathematical Calculations**
* 🧠 **Step-by-Step Planning**

This project demonstrates how **LLMs, tool calling, and LangGraph workflows** can be combined to build a practical tool-aware AI assistant.

---

## ✨ Key Features

| Feature                          | Description                                                            |
| -------------------------------- | ---------------------------------------------------------------------- |
| 🧠 **Intelligent Query Routing** | Determines whether a query requires a tool or can be answered directly |
| 🌤️ **Weather Tool**             | Retrieves weather information when required                            |
| 🔎 **Web Search Tool**           | Searches the web for information that requires external knowledge      |
| 🧮 **Calculator Tool**           | Handles mathematical calculations accurately                           |
| 🧠 **Planning Tool**             | Breaks complex tasks into structured steps                             |
| 🔗 **Tool Calling**              | Allows the LLM to interact with external capabilities                  |
| 🕸️ **LangGraph Workflow**       | Controls the flow between the assistant and available tools            |
| ⚡ **Groq Llama**                 | Provides fast LLM inference                                            |
| 💬 **Interactive Chat**          | Simple conversational interface for interacting with the assistant     |

---

# 🧠 How It Works

The assistant follows a **tool-aware workflow** rather than blindly calling tools.

```text
                    👤 USER
                       │
                       ▼
                 💬 User Query
                       │
                       ▼
              ┌─────────────────┐
              │    LLM Agent    │
              │   Groq Llama    │
              └────────┬────────┘
                       │
                Decide what to do
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Direct       Use Tool      Plan Task
       Answer          │
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      🌤️ Weather   🔎 Web Search  🧮 Calculator
                       │
                       ▼
                Tool Result
                       │
                       ▼
                 🤖 LLM Agent
                       │
                       ▼
                 💬 Final Answer
```

The key idea is simple:

> **The LLM decides when a tool is actually needed.**

For example:

```text
"What is LangGraph?"
        │
        ▼
   Direct Answer
```

But:

```text
"What is the weather in Delhi?"
        │
        ▼
   Weather Tool
        │
        ▼
   Final Answer
```

And:

```text
"Calculate 458 × 27"
        │
        ▼
   Calculator Tool
        │
        ▼
   Final Answer
```

---

# 🔄 LangGraph Workflow

LangGraph is used to manage the interaction between the LLM and available tools.

The workflow can be represented as:

```text
        👤 User Query
              │
              ▼
        🧠 Agent Node
              │
              ▼
       Tool Required?
          /       \
        No         Yes
        │           │
        ▼           ▼
   Direct Answer  Tool Node
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Weather   Web Search  Calculator
                    │
                    ▼
                Tool Result
                    │
                    ▼
               🧠 Agent Node
                    │
                    ▼
              Final Response
```

This allows the application to maintain a structured workflow instead of implementing tool usage as a collection of independent function calls.

---

# 🛠️ Available Tools

## 🌤️ Weather Tool

Used when the user asks for current weather information.

Example:

```text
What's the weather in Delhi today?
```

The agent identifies that external weather information is required and routes the request to the weather tool.

---

## 🔎 Web Search Tool

Used when the assistant needs information from the web.

Example:

```text
What are the latest developments in LangGraph?
```

The assistant can route the query through the web-search tool rather than relying only on the LLM's existing knowledge.

---

## 🧮 Calculator Tool

Used for mathematical calculations.

Example:

```text
Calculate 1256 × 87 + 450
```

The calculator tool performs the computation and returns the result to the agent.

---

## 🧠 Planning Tool

Used when a task requires multiple steps.

Example:

```text
Plan a 5-day trip to Rajasthan.
```

Instead of immediately producing an unstructured answer, the planning capability can break the task into logical steps before generating the final response.

---

# 💡 Tool Routing Examples

### Simple Question

```text
User
 │
 ▼
"What is RAG?"
 │
 ▼
LLM
 │
 ▼
Direct Answer
```

### Weather Query

```text
User
 │
 ▼
"Weather in Mumbai?"
 │
 ▼
LLM
 │
 ▼
🌤️ Weather Tool
 │
 ▼
Weather Result
 │
 ▼
LLM
 │
 ▼
Final Answer
```

### Mathematical Query

```text
User
 │
 ▼
"Calculate 789 × 45"
 │
 ▼
LLM
 │
 ▼
🧮 Calculator
 │
 ▼
Result
 │
 ▼
LLM
 │
 ▼
Final Answer
```

### Web Search Query

```text
User
 │
 ▼
"Search the web for..."
 │
 ▼
LLM
 │
 ▼
🔎 Web Search
 │
 ▼
Search Results
 │
 ▼
LLM
 │
 ▼
Final Answer
```

---

# 🧰 Tech Stack

### 🤖 AI & LLM

* **Groq** — Fast LLM inference
* **Llama** — Large Language Model
* **LangChain** — LLM and tool integration
* **LangGraph** — Agent workflow orchestration

### 🔧 Tools

* 🌤️ Weather Tool
* 🔎 Web Search
* 🧮 Calculator
* 🧠 Planning

### 🐍 Development

* Python

---

# 🚀 Getting Started

Follow the steps below to run the project locally.

## 1️⃣ Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv langgraph_env
```

### Windows

```bash
langgraph_env\Scripts\activate
```

### macOS / Linux

```bash
source langgraph_env/bin/activate
```

---

## 2️⃣ Install Dependencies

Install the required packages:

```bash
pip install langgraph langchain langchain-groq langchain-community python-dotenv requests
```

> Depending on the specific implementation of the tools, additional packages or APIs may be required.

---

# 🔐 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory.

Add your required API keys:

```env
GROQ_API_KEY=your_groq_api_key
```

If your web search or weather tools use external APIs, add their corresponding keys as required.

> ⚠️ **Never commit your `.env` file or API keys to GitHub.**

Add the following to `.gitignore`:

```gitignore
.env
langgraph_env/
__pycache__/
*.pyc
```

---

# 🔑 4️⃣ Get Your Groq API Key

The project uses Groq for LLM inference.

Create an API key from the Groq developer console and add it to your `.env` file.

---

# ▶️ 5️⃣ Run the Application

Run the assistant using:

```bash
python main.py
```

The application will start the interactive chat workflow.

---

# 💬 Example Queries

Try asking:

### 🧠 General Question

```text
What is Retrieval Augmented Generation?
```

### 🌤️ Weather

```text
What's the weather in Mumbai?
```

### 🔎 Web Search

```text
Search the web for the latest LangGraph features.
```

### 🧮 Calculation

```text
Calculate 4567 * 234.
```

### 🧠 Planning

```text
Create a step-by-step plan to build a RAG application.
```

The assistant determines whether each query requires a tool and routes it accordingly.

---

# 🧠 Why Use LangGraph?

A basic LLM application might look like:

```text
User
 │
 ▼
LLM
 │
 ▼
Response
```

Tool-using agents introduce additional capabilities:

```text
                 User
                  │
                  ▼
                 LLM
                  │
          ┌───────┼───────┐
          ▼       ▼       ▼
       Weather   Search Calculator
          │       │       │
          └───────┼───────┘
                  ▼
                 LLM
                  │
                  ▼
               Response
```

LangGraph provides a structured way to represent and control this workflow.

It makes the interaction between the **agent, tools, and state** explicit and easier to extend.

---

# 🎯 What This Project Demonstrates

This project provides practical experience with:

* Agentic AI
* LangGraph
* LangChain
* LLM tool calling
* Tool routing
* Agent workflows
* Conditional execution
* External API integration
* Groq LLM inference
* Multi-step task planning
* Conversational AI
* State-based AI workflows

---

# 🔮 Future Enhancements

The architecture can be extended with additional tools and capabilities.

### 📅 Calendar Tool

Allow the assistant to create and manage calendar events.

### 📧 Email Tool

Read, summarize, and draft emails through an email integration.

### 📚 RAG Tool

Connect the assistant to a private knowledge base and allow it to retrieve information from documents.

### 🗃️ Database Tool

Allow the agent to query structured databases using natural language.

### 🌐 Browser Agent

Add richer browsing capabilities for research-oriented tasks.

### 🧠 Memory

Add persistent conversation memory so the assistant can remember relevant information across sessions.

---

# 🚀 What Makes ToolPilot AI Different?

ToolPilot AI isn't designed to use a tool for every question.

Its core principle is:

```text
              USER QUERY
                  │
                  ▼
            🧠 UNDERSTAND
                  │
                  ▼
          ┌───────┴───────┐
          │               │
     Tool Needed?       No Tool
          │               │
         Yes              │
          │               │
          ▼               ▼
    Select Tool       Direct Answer
          │
          ▼
      Execute Tool
          │
          ▼
      Tool Result
          │
          ▼
    Generate Answer
```

This creates a more flexible AI assistant where **reasoning and tool usage are separated**, allowing the system to choose the appropriate capability based on the user's request.

---

# ⭐ If You Like This Project

If you find this project useful or interesting, consider giving the repository a ⭐.

Contributions, suggestions, and improvements are welcome!

---

## 📜 License

This project is intended for educational and demonstration purposes.
