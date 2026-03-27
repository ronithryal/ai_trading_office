import os
import sys

STYLE_CARD = """
- GOAL: Neutral, factual rolling tape of market-moving news.
- FORMAT: Timestamp; Headline; 1–3 sentence summary; Affected Assets; Tags.
"""

def generate_prompt(context_str):
    return f"""
    You are the reuters_news_agent persona.
    {STYLE_CARD}
    CONTEXT: {context_str}
    Generate a concise tape of breaking news items.
    """
