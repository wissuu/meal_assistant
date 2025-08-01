from fastapi import APIRouter, HTTPException
from typing import List
from src.db.meals_repository import log_meal
from src.ai.agent import get_meal_suggestions_command, MealPlanningChat
from src.models.food import FoodItem
from src.models.api import (
    MealSearchRequest, MealSearchResponse,
    AddMealRequest, AddMealResponse,
    ChatRequest, ChatResponse
)

router = APIRouter()

chat_session = MealPlanningChat()

@router.get("/meals/search", response_model=MealSearchResponse)
async def search_meals(
    meal_type: str = "breakfast",
    target_protein: float = 30,
    target_calories: int = 400
):
    """Search for meal suggestions based on parameters."""
    try:
        suggestions = get_meal_suggestions_command(meal_type, target_protein, target_calories)
        return MealSearchResponse(
            suggestions=suggestions if isinstance(suggestions, list) else [str(suggestions)],
            meal_type=meal_type,
            target_protein=target_protein,
            target_calories=target_calories
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get meal suggestions: {str(e)}")

@router.post("/meals", response_model=AddMealResponse)
async def add_meal(request: AddMealRequest):
    """Add a meal with food items."""
    try:
        results = []
        for food_item in request.food_items:
            result = log_meal(request.meal_type, food_item)
            results.append(result)
        
        return AddMealResponse(
            message=f"Successfully added {len(request.food_items)} food items to {request.meal_type}",
            success=True
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add meal: {str(e)}")

@router.post("/chat", response_model=ChatResponse)
async def chat_with_assistant(request: ChatRequest):
    """Chat with the meal planning assistant."""
    try:
        response = chat_session.get_response(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get chat response: {str(e)}")

@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}