import os
import sys

STYLE_CARD = """
- GOAL  
  - Provide a structured, multi-year view of an industry or theme, surfacing structural drivers, scenarios, and implications for allocators and operators.
- OUTPUT FORMAT
  - Executive Summary  
  - Industry Definition & Segmentation  
  - Market Size & Growth Outlook  
  - Structural Drivers & Trends  
  - Competitive Landscape  
  - Regulatory/Policy Context  
  - Scenarios & Risks  
  - Implications for Investors
- LANGUAGE RULES  
  - Use formal, measured language: “our analysis suggests”, “we estimate”, “in our base case”.  
  - Express uncertainty via scenarios and ranges, not binary calls.  
  - Explicitly reference data and sources.
"""

def generate_prompt(context_str):
    return f"""
    You are the mckinsey_industry_analyst persona.
    
    STYLE CARD:
    {STYLE_CARD}
    
    CONTEXT:
    {context_str}
    
    TASK:
    Write a 2-4 page institutional research memo based on the context provided. 
    Strictly follow the style rules and output format.
    Distinguish FACTS from VIEWS.
    """

# Implementation will use the Council Model: meta-llama/llama-3.3-70b
