import unittest
from unittest.mock import patch, MagicMock, ANY, call
from src.db.meals_repository import log_meal, init_db
from src.models.food import FoodItem

class TestLogMeal(unittest.TestCase):
    @patch("src.db.meals_repository.sqlite3.connect")
    def test_log_meal(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        meal_type = "Lunch"
        food_item = FoodItem(
            name="Chicken", 
            protein=30, 
            carbs=0, 
            fat=5, 
            fibre=0
        )

        result = log_meal(meal_type, food_item)

        mock_cursor.execute.assert_called_once()
        call_args = mock_cursor.execute.call_args[0]
        
        assert call_args[0] == "INSERT INTO meals (timestamp, meal_type, food_name, protein, carbs, fat, fibre) VALUES (?, ?, ?, ?, ?, ?, ?)"
        assert call_args[1][1:] == ("Lunch", "Chicken", 30, 0, 5, 0)  # Skip timestamp

        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()
        
        assert "Successfully logged Chicken as Lunch" in result

class TestInitDb(unittest.TestCase):
    @patch("src.db.meals_repository.sqlite3.connect")
    def test_init_db(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        init_db()

        expected_create_sql = """
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
    """
        mock_cursor.execute.assert_has_calls([call(expected_create_sql)])
        
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()