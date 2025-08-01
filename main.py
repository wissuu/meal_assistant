import typer
from src.db.meals_repository import init_db, log_meal
from src.ai.agent import get_meal_suggestions_command, MealPlanningChat
from src.models.food import FoodItem

app = typer.Typer()

@app.command()
def init():
    """Initialize the database."""
    init_db()
    typer.echo("Database initialized.")

@app.command()
def search(meal_type: str = "breakfast", target_protein: float = 30, target_calories: int = 400):
    """Search for new meals."""
    get_meal_suggestions_command(meal_type, target_protein, target_calories)

@app.command()
def chat():
    """Start an interactive chat session for meal planning."""
    typer.echo("🍽️  Welcome to Meal Planning Chat!")
    typer.echo("Tell me about your meal preferences. Type 'quit' to exit.\n")
    
    chat_session = MealPlanningChat()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                typer.echo("AI: Thanks for using Meal Planning Chat! Goodbye! 👋")
                break
            
            if not user_input:
                continue
                
            response = chat_session.get_response(user_input)
            typer.echo(f"AI: {response}\n")
            
        except KeyboardInterrupt:
            typer.echo("\nAI: Thanks for using Meal Planning Chat! Goodbye! 👋")
            break
        except Exception as e:
            typer.echo(f"Error: {str(e)}")
            typer.echo("Please try again or type 'quit' to exit.")

@app.command()
def add(meal_type: str):
    """Add a meal with macro info manually."""
    food_items = capture_items()
    for food_dict in food_items:
        food_item = FoodItem(**food_dict)
        result = log_meal(meal_type, food_item)
        typer.echo(result)

def capture_items():
    items = []

    while True:
        name = input("Food name: ")

        if not name:
            break

        protein = float(input("Protein: "))
        carbs = float(input("Carbs: "))
        fat = float(input("Fat: "))
        fibre = float(input("Fibre: "))

        items.append({"name": name, "protein": protein, "carbs": carbs, "fat": fat, "fibre": fibre})
    
    return items

if __name__ == "__main__":
    app()