# AI Trading Office 🏛️

**An AI-native, solo-founder institutional research and trading engine.**

This project allows a solo operator to run a high-conviction research desk and brand using agentic LLM workflows. Built with **Antigravity** and following **Boris Cherny's best practices** for building in public.

## 🌟 The Vision
To build an institutional-grade investment brand by leveraging a multi-agent "Research Council" that synthesizes diverse perspectives into high-conviction trade plans.

## 🏗️ Architecture
The system follows a 3-layer intelligence pattern:
1. **Intelligence Layer:** Broad scanning of "online chatter" (X, Reddit, forums) and deep-dive sources (McKinsey, Clouded Judgement, Artemis) into a centralized `research_inbox`.
2. **Research Council (Personas):** 8 specialized AI agents (McKinsey, Equity Research, SaaS, Crypto, X-Thread, Macro, Reuters, CNBC) each providing style-coded memos.
3. **Consensus Layer:** An **LLM Council** cross-critiques the research before a **Chairman agent** (GPT 5.4) synthesizes the final "Gold Standard" report.

## 🛠️ Tech Stack
- **Core:** Python (Async/Modular)
- **Database:** SQLite (Research Inbox)
- **Models:** OpenRouter (Gemini 3 Flash, Qwen 2.5-72B, DeepSeek-R1, Llama-3.3-70B, Hermes-4-70B, GPT-5.4)
- **Environment:** Dedicated Antigravity Skills for agent orchestration.

## 🚀 Getting Started
### 1. Configure
Create your `.env` from the skeleton:
```bash
cp .env.example .env
# Add your OpenRouter API Key
```

### 2. Physical Ingestion
Add your first high-conviction sources or snippets manually:
```bash
python3 ingestion/manual_ingest.py "Theme Title" "Data Content" "Source URL"
```

### 3. Trigger Research
Activate the council via the orchestrator (internal skill logic):
```bash
python3 agents/research_council_entry.py "Target Theme"
```

## 📜 Project Logs
We believe in radical transparency. Track our progress through:
- [Engineering Milestones (eng.md)](eng.md)
- [Product Decisions & Pivots (product.md)](product.md)

## ⚖️ License
MIT
