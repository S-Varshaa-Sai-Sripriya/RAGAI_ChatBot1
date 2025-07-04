# 🧠 Local RAG-Based AI Agent with Ollama, LangChain, and ChromaDB

![Gemini_Generated_Image_znlozznlozznlozz](https://github.com/user-attachments/assets/aa94bf48-3a64-477c-b238-83b295b2f826)

An end-to-end Retrieval-Augmented Generation (RAG) system built entirely on local infrastructure using Ollama, LangChain, and ChromaDB. 
This lightweight AI agent performs context-grounded document question answering by embedding and retrieving structured data (CSV) and generating responses through local LLMs—without reliance on cloud APIs or internet connectivity.

---

## 🚀 Project Overview

This agent demonstrates a fully offline, privacy-preserving LLM application by:

- Indexing CSV data via vector embeddings using MXB AI
- Storing vectors in ChromaDB for fast similarity retrieval
- Retrieving top-k context from documents based on user queries
- Generating coherent responses with a locally deployed LLaMA 3.2 model via AMA
- Orchestrating the pipeline using LangChain's prompt chaining and abstraction modules

---

## 🎯 Core Highlights

- ⚡ **100% Local RAG System** – No OpenAI, no cloud, no tokens
- 📦 **Modular Python Architecture** – Isolated components for ingestion, vectorization, retrieval, and generation
- 💬 **Dynamic Prompt Injection** – Factual grounding with LangChain’s template engine
- 🧠 **Efficient Vector Search** – High-performance similarity queries via ChromaDB
- 🛠️ **Model Deployment with AMA** – Plug-and-play LLM and embedding model loading on local hardware
- 🧪 **Real-World Dataset** – Applied on restaurant reviews (CSV) with open-ended user queries
- 👩‍💻 **Developer Productivity** – Boosted with GitHub Copilot throughout iterative development

---

## 🧪 Key Concepts Demonstrated

| Concept                             | Description |
|-------------------------------------|-------------|
| **Retrieval-Augmented Generation**  | Uses vector store to fetch contextual data before prompting |
| **Vector Embedding**                | MXB AI model converts documents into dense vectors |
| **Local LLM Deployment**            | AMA framework loads LLaMA 3.2 on CPU/GPU |
| **Prompt Chaining (LangChain)**     | Injects relevant context into templated LLM prompts |
| **Persistence & Efficiency**        | Avoids recomputation by persisting ChromaDB index |
| **Structured Reasoning**            | Enables controlled document-driven response generation |

---

> 📚 This project is a learning-based implementation

