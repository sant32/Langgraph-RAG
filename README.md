# 🧠 Agentic Corrective RAG System (LangGraph + FastAPI)

> A production-oriented **Agentic AI system** that goes beyond traditional RAG by **evaluating its own retrieval quality**, **dynamically routing between internal and external knowledge**, and **refining context at sentence level**.

---

# 🚀 Why This Project Matters

Most RAG systems:

* ❌ Blindly trust retrieved documents
* ❌ Fail when retrieval is weak
* ❌ Cannot adapt to missing or ambiguous context

---

### ✅ This system solves that:

* Evaluates retrieval quality using LLM
* Decides whether to:

  * Trust internal knowledge
  * Fetch external data
  * Combine both
* Refines context before answering

---

# 🏗️ System Architecture (Agentic Flow)

                ┌──────────────────────┐
                │     User Query       │
                └──────────┬───────────┘
                           ↓
                ┌──────────────────────┐
                │    Retriever (RAG)   │
                └──────────┬───────────┘
                           ↓
        ┌────────────────────────────────────┐
        │  LLM-based Document Evaluation     │
        │  (score each chunk: 0.0 → 1.0)     │
        └──────────┬───────────┬────────────┘
                   │           │
        ┌──────────▼───┐   ┌───▼──────────┐
        │   CORRECT    │   │  INCORRECT   │
        │ (trust docs) │   │ (use web)    │
        └──────┬───────┘   └──────┬───────┘
               │                  │
               │         ┌────────▼────────┐
               │         │  Web Search     │
               │         │ (Query Rewrite) │
               │         └────────┬────────┘
               │                  │
               └────────┬─────────┘
                        ↓
              ┌──────────────────────┐
              │ Context Refinement   │
              │ (Sentence Filtering) │
              └──────────┬───────────┘
                         ↓
              ┌──────────────────────┐
              │   Final Answer       │
              └──────────────────────┘

---

# 🧠 Key Features

## 🔍 1. Self-Evaluating Retrieval (Core Innovation)

* Each retrieved chunk is scored using LLM
* Structured output:

  * `score (0.0 – 1.0)`
  * `reason`

### Decision Logic:

* `> 0.7` → ✅ Reliable (CORRECT)
* `< 0.3` → ❌ Irrelevant (INCORRECT)
* Otherwise → ⚠️ Ambiguous

---

## 🔀 2. Adaptive Routing (Agentic Behavior)

Instead of static pipelines:

RAG → Answer ❌


This system does:

RAG → Evaluate → Decide → Adapt → Answer ✅

---

## ✂️ 3. Sentence-Level Context Refinement

* Documents are split into sentences
* Each sentence is validated using LLM
* Only relevant information is retained

👉 Reduces noise and hallucination

---

## 🌐 4. Web-Augmented Intelligence

* Automatically triggers web search when:

  * Retrieval fails
  * Context is insufficient
* Uses query rewriting for better results

---

## 🔄 5. Hybrid Knowledge Fusion

Combines:

* Chroma (Cloud) → Managed vector database
* 🌐 External knowledge (Tavily Search)

---

## ⚡ 6. Async Document Processing (Redis Queue)

* PDF uploads processed in background
* Scales independently from API

---

# 🛠️ Tech Stack

* **LangGraph** → Agent orchestration
* **LangChain** → RAG + structured outputs
* **Mistral AI** → LLM reasoning + evaluation
* **Chroma Cloud** → Managed vector database
* **Tavily** → Web search
* **FastAPI** → Backend APIs
* **Redis (RQ)** → Background jobs
* **LangSmith** → LLM observability & tracing


---

# 📊 Observability & Tracing

This project integrates **LangSmith** for end-to-end observability of the agent workflow:

- 🔍 Trace every step of the LangGraph execution
- 🧠 Debug LLM decisions (retrieval, evaluation, routing)
- 🛠️ Inspect tool usage and intermediate states
- 📈 Monitor performance and latency

👉 Enables **production-grade debugging and monitoring of agent behavior**

---

# ⚙️ Setup

uv sync
uvicorn main:app --reload

---


# 🧪 Example Queries

* “What is machine learning?”
* “Latest AI trends”
* “Explain reinforcement learning from the PDF”

---

# ⚠️ Limitations

* No persistent memory
* No streaming responses

---

# 🔮 Future Improvements

* 🧠 Memory (Redis / Vector memory)
* 🧩 Planner + Executor architecture
* ⚡ Streaming responses
* 🔍 Hybrid retrieval (BM25 + vector)
* 📊 Observability (tracing, logs)

---

# 🆚 Why This Is Better Than Basic RAG

| Feature                  | Basic RAG | This System |
|------------------------|----------|------------|
| Retrieval Evaluation    | ❌        | ✅          |
| Adaptive Routing        | ❌        | ✅          |
| Web Augmentation        | ❌        | ✅          |
| Context Refinement      | ❌        | ✅          |
| Agentic Behavior        | ❌        | ✅          |
| Cloud Vector DB         | ❌        | ✅          |


---

# 👨‍💻 Author

**Santosh Sakre**
