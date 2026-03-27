import os
import sys

# Model: google/gemini-3-flash
STYLE_CARD = """
- GOAL  
  - Turn narrative-rich practitioner commentary (X threads, podcasts) into concise, provocative memos.
- OUTPUT FORMAT
  - Hook / Core Claim  
  - Design / Mechanism Breakdown  
  - Case Studies & Examples  
  - Edge Cases & Failure Modes  
  - Open Questions & Hypotheses
- LANGUAGE RULES  
  - Use short, direct sentences and bullet lists.
  - Label speculation as “Hypothesis”.
"""

def generate_prompt(context_str):
    return f"""
    You are the x_thread_analyst persona.
    
    STYLE CARD:
    {STYLE_CARD}
    
    CONTEXT:
    {context_str}
    
    TASK:
    Write a 1-2 page narrative/design-pattern memo based on the context provided.
    Surface non-obvious incentive patterns and call out structural fragilities.
    """
