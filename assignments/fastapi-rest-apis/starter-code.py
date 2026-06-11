"""
FastAPI REST API Starter Code
Build a complete REST API for managing items
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI(title="Item Management API")

# TODO: Define your data model here (Pydantic BaseModel)
# Example structure: id, name, description, price


# TODO: Create an in-memory list to store items
# items = []


# TODO: Implement GET /items endpoint
# Should return all items


# TODO: Implement GET /items/{item_id} endpoint
# Should return a specific item by ID


# TODO: Implement POST /items endpoint
# Should accept a new item and add it to the list


# To run this application locally:
# 1. Install dependencies: pip install fastapi uvicorn
# 2. Run the server: uvicorn starter_code:app --reload
# 3. Visit http://localhost:8000/docs for interactive API documentation
