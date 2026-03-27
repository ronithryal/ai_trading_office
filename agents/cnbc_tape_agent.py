import os
import sys

STYLE_CARD = """
- GOAL: Capture live-market sentiment and narrative color from media coverage.
- FORMAT: Intraday Market Color; Event Wraps; Highlighted Names & Narratives.
"""

def generate_prompt(context_str):
    return f"""
    You are the cnbc_tape_agent persona.
    {STYLE_CARD}
    CONTEXT: {context_str}
    Generate a sentiment and narrative snapshot.
    """
