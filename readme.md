                         ┌─────────────────────┐
                         │       User          │
                         │ "Get order details" │
                         └──────────┬──────────┘
                                    │
                                    v
                         ┌─────────────────────┐
                         │    AI Application   │
                         │      FastAPI        │
                         └──────────┬──────────┘
                                    │
                                    v
                         ┌─────────────────────┐
                         │      Gemma LLM      │
                         │  Planner / Agent    │
                         └──────────┬──────────┘
                                    │
                           tool call request
                                    │
                                    v
                         ┌─────────────────────┐
                         │     MCP Client      │
                         └──────────┬──────────┘
                                    │
                              MCP Protocol
                                    │
                                    v
        ┌──────────────────────────────────────────────────┐
        │     mcp-enterprise-commerce-engine-server        │
        │                                                  │
        │  get_customers                                   │
        │  get_orders                                      │
        │  get_products                                    │
        │  get_categories                                  │
        │  get_suppliers                                   │
        │  get_shippers                                    │
        └──────────────────────┬───────────────────────────┘
                               │
                               v
                     Northwind API / DB

E:\GitHub\Python\mcp\
│
├── mcp-enterprise-commerce-engine-server
│ │
│ ├── app
│ │ ├── clients
│ │ ├── tools
│ │ ├── resources
│ │ ├── prompts
│ │ ├── config
│ │ └── server.py
│ │
│ └── ...
│
└── mcp-gemma-commerce-ai
│
├── app
│ ├── main.py
│ ├── config.py
│ │
│ ├── llm
│ │ └── gemma_client.py
│ │
│ ├── mcp
│ │ └── mcp_client.py
│ │
│ ├── agent
│ │ └── agent.py
│ │
│ ├── models
│ │ └── chat_models.py
│ │
│ └── services
│ └── chat_service.py
│
├── .env
├── requirements.txt
└── README.md

# MCP Gemma Commerce AI

AI application using:

- FastAPI
- Gemma
- Ollama
- MCP
- Enterprise Commerce MCP Server

## Architecture

User
|
v
FastAPI
|
v
Commerce Agent
|
v
Gemma
|
| decides which tools are required
v
MCP Client
|
v
Enterprise Commerce MCP Server
|
+-- Customers
+-- Orders
+-- Products
+-- Categories
+-- Suppliers
+-- Shippers
|
v
Tool Results
|
v
Gemma
|
v
Final Answer

## Prerequisites

Python 3.10+

Ollama

Enterprise Commerce MCP Server running at:

http://127.0.0.1:8000/mcp

## Install Ollama model

```powershell
ollama pull gemma3:4b
```
