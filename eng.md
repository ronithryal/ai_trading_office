# Engineering Logs (eng.md)

## 2026-03-27
### Milestones
- **Project Initialization:** Created `ai_trading_office/` directory structure (`data/`, `ingestion/`, `agents/`, `storage/`).
- **Data Layer:** Implemented `research_inbox` SQLite schema in `storage/db.py`. Added support for metadata nesting and signal classification.
- **Repository Pattern:** Created `InboxRepository` in `storage/inbox_repository.py` to abstract DB operations from agents.
- **Agentic Personas:** Built 8 modular persona agents (McKinsey, Equity Research, SaaS, Crypto, X-Thread, Macro, Reuters, CNBC) in `agents/` based on refined style cards.
- **Orchestration:** Implemented `ResearchCouncilOrchestrator` in `agents/research_council_entry.py` to manage multi-agent research workflows.
- **Ingestion Tools:** Created `manual_ingest.py` for direct user submission and `internet_chatter.py` for automated scanning logic.
- **Skill Codification:** Populated `SKILL_research_council.md` and `SKILL_trading_office.md` with operational protocols.
- **Python Packaging:** Added `__init__.py` files across all modules to ensure proper namespace management.
- **Traceability:** Implemented `InboxRepository` with full support for source-linking in reports.
- **Build in Public:** Initialized git repository and published to GitHub at `https://github.com/ronithryal/ai_trading_office`.

### Lessons
- **Schema Flexibility:** Using a `metadata_json` column in SQLite early on ensures we can handle diverse data from different MCPs/APIs without frequent migrations.
- **Async Orchestration:** Planning for `asyncio` in the orchestrator is critical for handling 8+ LLM calls in parallel later.
