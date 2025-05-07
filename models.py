from pydantic import BaseModel


class Item(BaseModel):
    # Definition de la classe Item qui herite de BaseModel
    id: int  # Ajout d'un champ id de type int
    name: str  # Ajout d'un champ name de type str
    price: float  # Ajout d'un champ price de type float
    in_stock: bool = True  # Ajout d'un champ in_stock avec une valeur par défaut de True