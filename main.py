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
    items = []
    while True:
        name = input("Food name (leave blank to stop): ")
        if not name:
            break
        protein = float(input("Protein: "))
        carbs = float(input("Carbs: "))
        fat = float(input("Fat: "))
        items.append({"name": name, "protein": protein, "carbs": carbs, "fat": fat})
    log_meal(meal_type, items)
    typer.echo(f"Added {len(items)} food(s) to {meal_type}.")

if __name__ == "__main__":
    app()