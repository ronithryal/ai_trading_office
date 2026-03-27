import sys
import os
import sqlite3
import json

# Add parent dir to path to import storage
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from storage.db import get_connection

def add_manual_item(title, content, source_url=None, topics="", priority="emphasis"):
    """
    Manually add a piece of research, a URL, or a snippet to the research_inbox.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO research_inbox (
        source_name, source_type, url, title, content, 
        primary_topics, priority, signal_type, signal_quality
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Manual Input",
        "manual",
        source_url,
        title,
        content,
        topics,
        priority,
        "alpha",
        "verified_user"
    ))
    
    item_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return item_id

if __name__ == "__main__":
    # Simple CLI for adding manual snippets
    if len(sys.argv) < 3:
        print("Usage: python manual_ingest.py <title> <content> [url] [topics]")
        sys.exit(1)
        
    title = sys.argv[1]
    content = sys.argv[2]
    url = sys.argv[3] if len(sys.argv) > 3 else None
    topics = sys.argv[4] if len(sys.argv) > 4 else ""
    
    item_id = add_manual_item(title, content, url, topics)
    print(f"Successfully added research item {item_id} to the inbox.")
