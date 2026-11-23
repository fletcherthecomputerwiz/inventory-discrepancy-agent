# Inventory Discrepancy Agent 
---
A multi-agent AI system that finds and investigates phantom inventory in retail stores: items the system shows as on hand but that aren't on the shelf, which stops automatic replenishment from reordering them. SQL rules flag likely cases, AI agents investigate the root cause, and a manager approves the recommended fix before any inventory record changes.

## How It Works
---
SQL-based detection flags suspect store/SKU pairs. AI agents then gather sales, receiving and adjustment evidence, retrieve the relevant store procedures with citations, and recommend a corrective action, with human approval required before any inventory change. Built on Python, Google Cloud (Gemini, Vertex AI, Cloud Run), LangGraph and ADK, using synthetic retail data.

# Inventory Discrepancy Agent

Detects and investigates phantom inventory in retail stores. Phantom inventory is a positive system on-hand count with no stock on the shelf. It suppresses automated replenishment and causes lost sales that never trigger an alert.

## How It Works

Deterministic SQL flags candidate store/SKU pairs by comparing sales velocity against on-hand history. A multi-agent workflow then gathers sales, receiving and adjustment evidence, retrieves the applicable store procedure with citations, and proposes a corrective action. All inventory writes require human approval and are audit-logged.

Built with Python, LangGraph, Google ADK, Gemini and Vertex AI, deployed on Cloud Run. Uses synthetic retail data.

