from pydantic import BaseModel
import requests
import os
from typing import Optional


class MealSuggestion(BaseModel):
    title: str
    calories: int
    protein: float
    carbs: float
    fat: float
    recipe_url: str


def get_meal_suggestions(
    meal_type: str,
    target_calories: Optional[int] = None,
    target_protein: Optional[float] = None,
    target_carbs: Optional[float] = None,
    target_fat: Optional[float] = None,
    dietary_restrictions: Optional[str] = None
) -> str:
    """
    Fetch meal data from Spoonacular API for the AI assistant to analyze and present.
    
    Args:
        meal_type: Type of meal (breakfast, lunch, dinner, snack)
        target_calories: Target calories per serving
        target_protein: Target protein in grams
        target_carbs: Target carbs in grams  
        target_fat: Target fat in grams
        dietary_restrictions: Comma-separated dietary restrictions (vegetarian, vegan, gluten-free, etc.)
    """
    
    api_key = os.getenv('SPOONACULAR_API_KEY')
    base_url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        'apiKey': api_key,
        'type': meal_type,
        'number': 8,
        'addRecipeNutrition': True,
        'addRecipeInstructions': True,
        'sort': 'popularity'
    }
    
    if target_calories:
        params['maxCalories'] = target_calories + 150
        params['minCalories'] = max(0, target_calories - 150)
    
    if target_protein:
        params['minProtein'] = max(0, target_protein - 10)
        params['maxProtein'] = target_protein + 10
        
    if target_carbs:
        params['minCarbs'] = max(0, target_carbs - 15)
        params['maxCarbs'] = target_carbs + 15
        
    if target_fat:
        params['minFat'] = max(0, target_fat - 8)
        params['maxFat'] = target_fat + 8
    
    if dietary_restrictions:
        params['diet'] = dietary_restrictions
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if not data.get('results'):
            return f"RECIPE_DATA: No recipes found for {meal_type} with specified criteria. User requested: calories={target_calories}, protein={target_protein}g, carbs={target_carbs}g, fat={target_fat}g, diet={dietary_restrictions}"
        
        recipe_data = []
        for recipe in data['results'][:5]:
            nutrition = recipe.get('nutrition', {})
            nutrients = {n['name']: round(n['amount'], 1) for n in nutrition.get('nutrients', [])}
            
            recipe_info = {
                'title': recipe['title'],
                'id': recipe['id'],
                'ready_in_minutes': recipe.get('readyInMinutes', 'N/A'),
                'servings': recipe.get('servings', 'N/A'),
                'calories': nutrients.get('Calories', 0),
                'protein': nutrients.get('Protein', 0),
                'carbs': nutrients.get('Carbohydrates', 0),
                'fat': nutrients.get('Fat', 0),
                'fiber': nutrients.get('Fiber', 0),
                'sugar': nutrients.get('Sugar', 0),
                'source_url': recipe.get('sourceUrl', ''),
                'spoon_url': f"https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-').lower()}-{recipe['id']}"
            }
            recipe_data.append(recipe_info)
        
        return f"RECIPE_DATA: Found {len(recipe_data)} {meal_type} recipes matching criteria (calories≈{target_calories}, protein≈{target_protein}g). Recipe details: {recipe_data}"
        
    except requests.RequestException as e:
        return f"RECIPE_DATA: API error - {str(e)}. Please provide general meal suggestions for {meal_type} with target calories={target_calories}, protein={target_protein}g."