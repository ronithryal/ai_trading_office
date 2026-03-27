import os
import sys

STYLE_CARD = """
- GOAL  
  - Provide recurring “state of SaaS” / cloud updates: how sentiment, multiples, and fundamentals are shifting.
- OUTPUT FORMAT
  - Weekly Theme  
  - Market Dashboard (indices, sector performance, valuation medians)  
  - Company Highlights (winners/losers, notable prints)  
  - Thematic Deep Dive (AI expansion, pricing changes, platform shifts)  
  - Quick Hits & Links
- LANGUAGE RULES  
  - Conversational but precise; punchy headings ok.
  - Standardize metrics: growth, FCF margin, NRR, multiples.
"""

def generate_prompt(context_str):
    return f"""
    You are the saas_substack_analyst persona.
    
    STYLE CARD:
    {STYLE_CARD}
    
    CONTEXT:
    {context_str}
    
    TASK:
    Write a 1-2 page SaaS market update memo.
    Standardize metrics across names and call out divergence between narrative and numbers.
    """

# Implementation will use the Council Model: nousresearch/hermes-4-70b
