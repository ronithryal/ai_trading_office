import os
import sys
import json
import asyncio
from typing import List, Dict

# Add paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from storage.inbox_repository import InboxRepository

class ResearchCouncilOrchestrator:
    def __init__(self):
        self.inbox = InboxRepository()
        self.personas = [
            "macro_economist",
            "reuters_news_agent",
            "cnbc_tape_agent",
            "mckinsey_industry_analyst",
            "equity_research_analyst",
            "saas_substack_analyst",
            "crypto_onchain_analyst",
            "x_thread_analyst"
        ]

    async def gather_context(self, theme: str, limit: int = 20) -> str:
        """
        Retrieves relevant research items and formats them as a context string.
        """
        items = self.inbox.get_items_by_topic(theme, limit=limit)
        if not items:
            # Fallback to recent items if theme search fails
            items = self.inbox.get_recent_items(limit=limit)
            
        context_parts = []
        for item in items:
            part = f"SOURCE: {item['source_name']} ({item['source_type']})\n"
            part += f"TITLE: {item['title']}\n"
            part += f"CONTENT: {item['content']}\n"
            part += "-" * 20
            context_parts.append(part)
        
        return "\n".join(context_parts)

    async def run_council(self, theme: str):
        """
        Main entry point to run the full council research for a theme.
        """
        print(f"Starting Research Council for theme: {theme}")
        context = await self.gather_context(theme)
        
        # In a real system, we would trigger the specific LLM calls here.
        # For now, we return the plan/status.
        
        memos = {}
        for persona in self.personas:
            # Dispatching to persona...
            memos[persona] = f"Pending memo for {persona} regarding {theme}"
            
        return {
            "theme": theme,
            "status": "memos_pending",
            "personas_engaged": self.personas,
            "context_summary": f"{len(context.split('-'*20))} sources found."
        }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python research_council_entry.py <theme>")
        sys.exit(1)
        
    theme = sys.argv[1]
    orchestrator = ResearchCouncilOrchestrator()
    result = asyncio.run(orchestrator.run_council(theme))
    print(json.dumps(result, indent=2))
