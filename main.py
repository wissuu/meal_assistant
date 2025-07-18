import typer
from meal_assistant.db.sqlite import init_db, log_meal

app = typer.Typer()

@app.command()
def init():
    """Initialize the database."""
    init_db()
    typer.echo("Database initialized.")

@app.command()
def add(meal_type: str):
    """Add a meal with macro info manually."""
    food_items = capture_items()
    log_meal(meal_type, food_items)
    typer.echo(f"Logged: ")
    for food in food_items:
        typer.echo(f"{food['name']}")

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