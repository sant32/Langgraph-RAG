# 🧠 Agentic RAG Chatbot with LangGraph

This project is an **Agentic AI chatbot** built using **LangGraph + LangChain**, capable of:

* 📄 Answering questions from a PDF (RAG)
* 🌐 Performing web search
* 🧮 Solving calculations
* 📈 Fetching stock prices

It uses a **tool-augmented LLM agent** with a **graph-based execution flow**.

---

# 🚀 Features

* ✅ Retrieval-Augmented Generation (RAG) over PDF
* ✅ Multi-tool support (Search, Calculator, Stock API)
* ✅ LangGraph-based agent workflow
* ✅ Tool routing using `tools_condition`
* ✅ Fast dependency management using `uv`

---

# 🏗️ Architecture

```
User Query
   ↓
Chat Node (LLM)
   ↓
tools_condition
   ├── Tool Call → Tool Node → Chat Node (loop)
   └── No Tool → END
```

---

# 🛠️ Tech Stack

* **LangGraph** – Graph-based agent orchestration
* **LangChain** – Tooling + RAG pipeline
* **Mistral AI** – LLM + Embeddings
* **FAISS** – Vector database
* **uv** – Fast Python package manager
* **Python** – Backend

---

# 📂 Project Structure

```
.
├── main.py
├── thebook.pdf
├── .env
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# ⚙️ Setup Instructions (Using uv)

## 1. Install uv

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```

or

```bash
pip install uv
```

---

## 2. Clone Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

## 3. Create Virtual Environment

```bash
uv venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
```

---

## 4. Install Dependencies

If you have `pyproject.toml`:

```bash
uv sync
```

Or manually:

```bash
uv add langchain langgraph mistralai faiss-cpu python-dotenv duckduckgo-search
```

---

## 5. Add Environment Variables

Create `.env` file:

```
MISTRAL_API_KEY=your_api_key_here
```

---

## 6. Run the Application

```bash
python main.py
```

---

# 🔧 Tools Implemented

## 📄 RAG Tool

* Semantic search over PDF using FAISS
* Retrieves relevant chunks

## 🌐 Web Search Tool

* DuckDuckGo integration for real-time data

## 🧮 Calculator Tool

* Supports: add, sub, mul, div

## 📈 Stock Price Tool

* Uses Alpha Vantage API

---

# 🧠 How It Works

1. PDF is loaded and split into chunks
2. Embeddings are created and stored in FAISS
3. User query is passed to LLM
4. `tools_condition` decides:

   * Use tool → execute → loop back
   * No tool → return response

---

# 🧪 Example Queries

```
What is 3 + 4
Summarise the PDF
Latest AI news
AAPL stock price
```

---

# ⚠️ Known Limitations

* Tool usage depends on prompt quality
* No memory (stateless agent)
* RAG can be improved with re-ranking
* No streaming yet

---

# 🔮 Future Improvements

* Add streaming responses
* Add Redis/Postgres memory
* Improve RAG (compression, hybrid search)
* Add planner (multi-agent system)
* Deploy using FastAPI

---

# 🚀 Next Steps

To make this production-ready:

* Add **Agent Memory**
* Add **Planner + Executor architecture**
* Enable **parallel tool execution**
* Add **frontend (React / Streamlit)**

---

# 👨‍💻 Author

Built by **Santosh Sakre**

---


