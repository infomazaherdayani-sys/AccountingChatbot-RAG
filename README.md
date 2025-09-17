# AccountingChatbot-RAG

A Retrieval-Augmented Generation (**RAG**) demo built with **Python**, **LangChain**, and **OpenAI**, designed to work with **accounting documents stored in SQL Server** as JSON.  

This project demonstrates how to build an **AI-powered accounting assistant** that can answer financial/accounting questions by retrieving relevant documents from a SQL database and combining them with a Large Language Model (LLM).

---

## 🚀 Features
- Store accounting documents as **JSON** in SQL Server  
- Convert JSON documents into **vector embeddings** using OpenAI  
- Use **LangChain** with **FAISS** for vector search  
- Ask natural language questions about accounting data  
- Get AI-generated answers based on your own financial records  

---

## 📂 Example JSON Documents

```json
{
  "DocumentId": "DOC-1001",
  "Description": "Salary payment for employees",
  "Amount": 50000,
  "AccountCode": "501",
  "DocumentDate": "2025-09-01"
}
