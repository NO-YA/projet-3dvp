from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()


# definie le modele d'item ("produit")
class Item(BaseModel):
    id: int
    name: str
    price: float


items: List[Item] = []
# ici nous allons ajouter un produit


@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return item


# ici ont recupere tous les produits


@app.get("/items/", response_model=List[Item])
def read_items():
    return items


# dans cette partie on modifie en feonction de ses parametres


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for i in range(len(items)):
        if items[i].id == item_id:
            items[i] = item
            return item
    return {"error": "Item not found"}


# cette partie permet de supprimer un produit


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    items = [item for item in items if item.id != item_id]
    return {"message": "Item deleted successfully"}