# Inventory Discrepancy Agent 
---
A multi agent AI system that detects and investigates phantom inventory in retail stores, where system on-hand counts show stock that isn’t on the shelf and so blocks automatic replenishment. 

# How It Works
---
SQL-based detection flags suspect store/SKU pairs. AI agents then gather sales, receiving and adjustment evidence, retrieve the relevant store procedures with citations, and recommend a corrective action, with human approval required before any inventory change. Built on Python, Google Cloud (Gemini, Vertex AI, Cloud Run), LangGraph and ADK, using synthetic retail data.