# 🥗 Meal Assistant CLI

A natural-language meal tracking and macro-balancing assistant, built in Python.  
Log what you eat in plain English, track your protein/carb/fat/fibre intake, and get smart suggestions for the rest of your day.

## 💡 Why I Built This

I wanted to learn Python by solving a real problem: planning meals based on macros, something I'm interested in in my personal life.  
This project combines CLI tooling, NLP parsing, data modeling, and food APIs into a single, testable, practical tool.

## 🧪 Features

- **One-shot meal search**: Quick meal suggestions with specific protein/calorie targets
- **Interactive AI chat**: Natural conversation to find and store meals in your database
- Track daily macros and compare against your goals

## 🛠️ Tech Stack

- Python 3.11
- Typer (CLI)
- LangGraph + LangChain (AI agent)
- Claude 3 Sonnet (via AWS Bedrock)
- SQLite database
- pydantic (models)
- pytest

## 🧭 Roadmap

- [ ] FastAPI wrapper
- [ ] React UI for logging meals and seeing trends
- [ ] Personalization (macro targets, food preferences)
- [ ] Graph view of macro distribution over time

## 📸 CLI Demo

```bash
# One-shot meal search
$ python main.py search --meal-type breakfast --target-protein 30 --target-calories 400
> Greek yogurt parfait with granola and berries
> Protein: 30g | Calories: 395 | Carbs: 45g | Fat: 12g

# Interactive AI chat for meal planning
$ python main.py chat
> Hi! I can help you find meals and store them in your database. What are you looking for?

User: I need a high protein lunch around 500 calories
Assistant: I found some great options! How about grilled chicken salad with quinoa?
Protein: 35g | Calories: 485 | Carbs: 28g | Fat: 18g
Would you like me to store this meal in your database?

User: Yes, store it
Assistant: Great! I've stored "Grilled chicken salad with quinoa" in your meal database.
```

## How to's

### Database commands

sqlite-utils rows meals.db meals

### Set up project

`pip install -e .` # Install in development mode`

`pip install -e ".[dev]"` # Install with dev dependencies
