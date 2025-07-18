import unittest
from unittest.mock import patch, MagicMock, ANY
from meal_assistant.db.sqlite import log_meal

class TestLogMeal(unittest.TestCase):
    @patch("meal_assistant.db.sqlite.sqlite3.connect")
    def test_log_meal(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Test data
        meal_type = "Lunch"
        food_items = [
            {"name": "Chicken", "protein": 30, "carbs": 0, "fat": 5, "fibre": 0},
            {"name": "Rice", "protein": 4, "carbs": 45, "fat": 1, "fibre": 2},
        ]

        log_meal(meal_type, food_items)

        expected_calls = [
            (
                "INSERT INTO meals (timestamp, meal_type, food_name, protein, carbs, fat, fibre) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (ANY, "Lunch", "Chicken", 30, 0, 5, 0),
            ),
            (
                "INSERT INTO meals (timestamp, meal_type, food_name, protein, carbs, fat, fibre) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (ANY, "Lunch", "Rice", 4, 45, 1, 2),
            ),
        ]
        calls = mock_cursor.execute.call_args_list

        assert len(calls) == 2

        assert calls[0][0][0].startswith("INSERT INTO meals")
        assert calls[0][0][1][1:] == ("Lunch", "Chicken", 30, 0, 5, 0)

        assert calls[1][0][0].startswith("INSERT INTO meals")
        assert calls[1][0][1][1:] == ("Lunch", "Rice", 4, 45, 1, 2)
        
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()