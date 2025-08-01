from pydantic import BaseModel
from typing import List, Optional
from .food import FoodItem


class MealSearchRequest(BaseModel):
    meal_type: str = "breakfast"
    target_protein: float = 30
    target_calories: int = 400


class MealSearchResponse(BaseModel):
    suggestions: List[str]
    meal_type: str
    target_protein: float
    target_calories: int


class AddMealRequest(BaseModel):
    meal_type: str
    food_items: List[FoodItem]


class AddMealResponse(BaseModel):
    message: str
    success: bool


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str