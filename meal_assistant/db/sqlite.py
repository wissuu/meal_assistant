import sqlite3
from datetime import datetime

DB_PATH = "meals.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            meal_type TEXT,
            food_name TEXT,
            protein REAL,
            carbs REAL,
            fat REAL
        )
    """)
    conn.commit()
    conn.close()


def log_meal(meal_type: str, food_items: list[dict]):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.now().isoformat()
    for food in food_items:
        c.execute(
            "INSERT INTO meals (timestamp, meal_type, food_name, protein, carbs, fat) VALUES (?, ?, ?, ?, ?, ?)",
            (now, meal_type, food["name"], food["protein"], food["carbs"], food["fat"])
        )
    conn.commit()
    conn.close()