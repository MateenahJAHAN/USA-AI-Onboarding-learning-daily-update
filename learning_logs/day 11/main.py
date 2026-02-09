from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory "database"
items = []

# Pydantic model
class Item(BaseModel):
    id: int
    name: str
    price: float

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}

@app.get("/items/")
def get_items():
    return items

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item created", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for i in range(len(items)):
        if items[i].id == item_id:
            items[i] = item
            return {"message": "Item updated", "item": item}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i in range(len(items)):
        if items[i].id == item_id:
            items.pop(i)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

