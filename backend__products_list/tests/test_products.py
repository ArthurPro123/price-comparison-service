import pytest
from app import app, db, Product
from tests.factories import ProductFactory

@pytest.fixture
def client():
    """Provides a test client for the Flask app."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_get_products_returns_empty_list_when_no_products_exist(client):
    """Returns an empty list when no products exist."""
    response = client.get('/products')
    assert response.status_code == 200
    assert response.json == {"products": []}

def test_get_products_returns_all_products(client):
    """Returns all products with their dealers."""
    product = ProductFactory(name="Laptop", dealers=["Store A", "Store B"])
    db.session.add(product)
    db.session.commit()

    response = client.get('/products')
    assert response.status_code == 200
    assert response.json == {
        "products": [{"product": "Laptop", "Dealers": ["Store A", "Store B"]}]
    }

def test_get_products_returns_multiple_products(client):
    """Returns multiple products with their dealers."""
    ProductFactory.create_batch(
        2,
        name="Product",
        dealers=["Store X", "Store Y"]
    )
    db.session.commit()

    response = client.get('/products')
    assert response.status_code == 200
    assert len(response.json["products"]) == 2

def test_get_products_handles_missing_dealers(client):
    """Returns products even if dealers list is empty."""
    product = ProductFactory(name="Mouse", dealers=[])
    db.session.add(product)
    db.session.commit()

    response = client.get('/products')
    assert response.status_code == 200
    assert response.json["products"][0]["Dealers"] == []
