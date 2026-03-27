import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "trading_office.db")

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # research_inbox table for multi-sourced intelligence
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS research_inbox (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_name TEXT NOT NULL,
        source_type TEXT,        -- newsletter, x_thread, reddit, mcp_search, api, manual
        url TEXT,
        title TEXT,
        content TEXT,           -- raw or summarized content
        created_at TEXT,        -- source timestamp
        ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        primary_topics TEXT,    -- comma-separated tags
        geography_focus TEXT,
        signal_type TEXT,       -- macro, institutional, alpha, chatter
        priority TEXT,          -- emphasis, normal, noise
        hype_risk TEXT,
        signal_quality TEXT,
        metadata_json TEXT      -- flexible extra data
    )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print(f"Database initialized at {DB_PATH}")
