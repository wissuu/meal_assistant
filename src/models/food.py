from pydantic import BaseModel
from typing import List

class FoodItem(BaseModel):
    name: str
    protein: float
    carbs: float
    fat: float
    fibre: float

class Meal(BaseModel):
    meal_type: str
    items: List[FoodItem]