---
name: research_council_writer
description: >
  Multi-agent research council that writes high-quality, institutional-grade
  investment research memos across macro, equities, SaaS, and crypto/on-chain domains.
version: 0.1.1
status: active
---

# Research Council Skill

## Overview
This skill orchestrates a multi-agent workflow to produce "Gold Standard" research. It uses a 3-stage process:
1. **Persona Memos:** 8 domain specialists write style-coded memos grounded in the `research_inbox` and broad intelligence.
2. **Cross-Critique:** An LLM Council of 5 diverse models (Gemini Flash, Qwen, DeepSeek, Llama, Hermes) reviews and identifies gaps.
3. **Chairman Synthesis:** A master model (GPT 5.4) synthesizes all memos and critiques into a unified report.

## Domain Specialists (Personas)
- **mckinsey_industry_analyst:** Structural industry trends and scenario-based framing.
- **equity_research_analyst:** Security-level deep dives (Thesis -> Business -> Valuation -> Risks).
- **saas_substack_analyst:** SaaS sentiment, multiples, and fundamental updates.
- **crypto_onchain_analyst:** On-chain data and protocol fundamentals (Artemis/Messari data).
- **x_thread_analyst:** Narrative, design-pattern, and practitioner-scout insights.
- **macro_economist:** Macro and policy baseline.
- **reuters_news_agent / cnbc_tape_agent:** Real-time news and sentiment "tape".

## Operational Rules
- **Grounding over Hype:** Every claim must be grounded in facts from the `research_inbox` (Source of Emphasis) or external search.
- **Traceability:** Final reports must include a "Sources & Traceability" section linking facts back to ingested items.
- **Institutional Tone:** Memos must maintain the formal, analytical tone defined in their respective style cards.

## Workflow Execution
- To trigger research: Provide a `theme` or `ticker`.
- Dispatch to `agents/research_council_entry.py`.
