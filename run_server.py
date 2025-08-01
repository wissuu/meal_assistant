#!/usr/bin/env python3
"""
Development server runner for the Meal Assistant API.
Run this file to start the FastAPI server with hot reloading.
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["src", "."]
    )