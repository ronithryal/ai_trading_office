import os
import sys
import json
import sqlite3
import datetime

# Add parent path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from storage.db import get_connection

class InboxRepository:
    @staticmethod
    def get_recent_items(limit=10, priority=None):
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        query = "SELECT * FROM research_inbox"
        params = []
        if priority:
            query += " WHERE priority = ?"
            params.append(priority)
        
        query += " ORDER BY ingested_at DESC LIMIT ?"
        params.append(limit)
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @staticmethod
    def get_items_by_topic(topic, limit=10):
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM research_inbox 
            WHERE primary_topics LIKE ? 
            ORDER BY ingested_at DESC LIMIT ?
        """, (f"%{topic}%", limit))
        
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @staticmethod
    def add_item(data):
        conn = get_connection()
        cursor = conn.cursor()
        
        keys = data.keys()
        columns = ", ".join(keys)
        placeholders = ", ".join(["?" for _ in keys])
        values = tuple(data.values())
        
        cursor.execute(f"INSERT INTO research_inbox ({columns}) VALUES ({placeholders})", values)
        
        item_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return item_id
