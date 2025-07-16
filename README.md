# 🥗 Meal Assistant CLI

A natural-language meal tracking and macro-balancing assistant, built in Python.  
Log what you eat in plain English, track your protein/carb/fat/fibre intake, and get smart suggestions for the rest of your day.

## 💡 Why I Built This

I wanted to learn Python by solving a real problem: planning meals based on macros, something I'm interested in in my personal life.  
This project combines CLI tooling, NLP parsing, data modeling, and food APIs into a single, testable, practical tool.

## 🧪 Features

- Log meals using natural language (`meal log "2 eggs and toast"`)
- Track daily macros and compare against your goals
- Get meal suggestions to hit your targets (e.g., 150g protein/day)

## 🛠️ Tech Stack

- Python 3.11
- Typer (CLI)
- JSON storage
- pydantic (models)
- pytest

## 🧭 Roadmap

- [ ] FastAPI wrapper
- [ ] React UI for logging meals and seeing trends
- [ ] Personalization (macro targets, food preferences)
- [ ] Graph view of macro distribution over time

## 📸 CLI Demo

```bash
$ meal log "2 scrambled eggs and a banana"
> Logged: scrambled eggs, banana
> Current total: Protein 14g | Carbs 25g | Fat 10g

$ meal status
> Today's goals: Protein 150g | Carbs 180g | Fat 60g
> So far:        Protein 54g | Carbs 90g | Fat 38g

$ meal suggest
> Try: grilled chicken breast with broccoli and quinoa
> Est. macros: Protein 45g | Carbs 30g | Fat 10g
```
