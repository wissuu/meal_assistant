from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.routes import router
from src.db.meals_repository import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize database
    print("Initializing database...")
    init_db()
    print("Database initialized successfully")
    yield
    # Shutdown: Add cleanup logic here if needed
    print("Shutting down...")


app = FastAPI(
    title="Meal Assistant API",
    description="A natural-language meal tracking and macro-balancing assistant",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(router)