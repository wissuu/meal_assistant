import sqlite3
from datetime import datetime
from src.models.food import FoodItem

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
            fat REAL,
            fibre REAL
        )
    """)
    conn.commit()
    conn.close()


def log_meal(meal_type: str, food_item: FoodItem) -> str:
    """
    Logs a meal item into the meals database.
    
    Args:
        meal_type: Type of meal (breakfast, lunch, dinner, snack)
        food_item: FoodItem object containing name and nutritional information
        
    Returns:
        Success message confirming the meal was logged
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        now = datetime.now().isoformat()
        
        c.execute(
            "INSERT INTO meals (timestamp, meal_type, food_name, protein, carbs, fat, fibre) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (now, meal_type, food_item.name, food_item.protein, food_item.carbs, food_item.fat, food_item.fibre)
        )
        conn.commit()
        conn.close()
        
        return f"Successfully logged {food_item.name} as {meal_type}. Nutrition: {food_item.protein}g protein, {food_item.carbs}g carbs, {food_item.fat}g fat, {food_item.fibre}g fiber."
        
    except Exception as e:
        return f"Error logging meal: {str(e)}"