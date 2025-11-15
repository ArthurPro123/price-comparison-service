import factory
from app import db, Product

class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Factory for creating Product test instances."""
    class Meta:
        model = Product
        sqlalchemy_session = db.session

    name = factory.Sequence(lambda n: f"Product {n}")
    dealers = factory.List(["Store A", "Store B"])
