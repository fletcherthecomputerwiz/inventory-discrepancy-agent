
# Inventory Discrepancy Agent

Detects and investigates phantom inventory in retail stores. Phantom inventory is a positive system on-hand count with no stock on the shelf. It suppresses automated replenishment and causes lost sales that never trigger an alert.

## How It Works

Deterministic SQL flags candidate store/SKU pairs by comparing sales velocity against on-hand history. A multi-agent workflow then gathers sales, receiving and adjustment evidence, retrieves the applicable store procedure with citations, and proposes a corrective action. All inventory writes require human approval and are audit-logged.

Built with Python, LangGraph, Google ADK, Gemini and Vertex AI, deployed on Cloud Run. Uses synthetic retail data.