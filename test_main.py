from fastapi.testclient import TestClient
from main import app  # Importez l'application FastAPI depuis le fichier main.py

client = TestClient(app)
# cree un client pour tester l'API


# Test de la création d'un item
def test_create_item():
    response = client.post(
        "/items/", json={"id": 1, "name": "Item 1", "price": 10.0}
    )  # il envoie une requete POST pour creer un produit
    assert response.status_code == 200  # il verifie que le code de statut repond 200
    assert response.json()["name"] == "Item 1"  # il verifie que le nom du produit est bien "Item 1"
    # il verifie que la reponse est bien le produit cree


# test la recuperation de tous les items par la riute get
def test_get_items():
    response = client.get(
        "/items/"
    )  # il envoie une requete GET pour recuperer tous les produits
    assert response.status_code == 200  # il verifie que le code de statut est 200
    assert type(response.json()) is list  # il verifie que la reponse est bien une liste


# ici ont va tester la M.AJ d'un produit
def test_update_item():
    response = client.put(
        "/items/1", json={"id": 1, "name": "XOXO", "price": 199.0}
    )  # il envoie une requete PUT pour modifier le produit
    assert response.status_code == 200  # il verifie que le code de statut est 200
    assert response.json()["name"] == "XOXO"  # il verifie que le nom du produit est bien "XOXO"
    # il verifie que la reponse est bien le produit modifie


# test la suppression d'un produit
def test_delete_item():
    response = client.delete(
        "/items/1"
    )  # il envoie une requete DELETE pour supprimer le produit
    assert response.status_code == 200  # il verifie que le code de statut est 200
    assert (
        response.json()["message"] == "Item deleted successfully"
    )  # il verifie que le message de reponse est bien "Item deleted successfully"