from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger
import os

app = Flask(__name__)

# Configure Swagger
app.config['SWAGGER'] = {
    "uiversion": 3,
    "openapi": "3.0.2",
    "info": {
    "title": "Product Dealer API",
    "version": "1.0",
        "description": "API for viewing products and their dealers"
    }
}

Swagger(app)

# Configure SQLAlchemy to use SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    dealers = db.Column(db.JSON, nullable=False)  # Store dealers as JSON

# Create tables (run once)
with app.app_context():
    db.create_all()
    # Insert sample data if the table is empty
    if not Product.query.first():
        products_data = [
            Product(name="Headphones", dealers=["Binglee", "DXC Electronics", "Bobay"]),
            Product(name="Laptop", dealers=["GH Computers", "Tech City", "Ez PC"]),
            Product(name="Mouse", dealers=["DXC Electronics", "Tech City"]),
            Product(name="Printer", dealers=["Binglee", "DXC Electronics", "Bobay", "GH Computers"])
        ]
        db.session.bulk_save_objects(products_data)
        db.session.commit()

# Enable CORS only in development
if os.getenv("RUNNING_MODE") == "development":
    CORS(
        app,
        resources={r"/*": {
            "origins": [
                "http://localhost:5000",  # Swagger UI
                "http://localhost:5001",  # Your frontend
                "https://editor.swagger.io"  # Swagger Editor
            ]
        }},
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"]
    )


@app.route('/products')
def get_products():
    """
    Get all products and their dealers
    ---
    tags:
      - Products
    responses:
      200:
        description: Get a list of products and their dealers
        content:
          application/json:
            schema:
              type: object
              properties:
                products:
                  type: array
                  items:
                    type: object
                    properties:
                      product:
                        type: string
                      Dealers:
                        type: array
                        items:
                          type: string
    """
    products = Product.query.all()
    return jsonify({"products": [{"product": p.name, "Dealers": p.dealers} for p in products]})

@app.route('/getdealers/<product>')
def get_dealers(product):
    """
    Get dealers for a specific product
    ---
    tags:
      - Dealers
    parameters:
      - name: product
        in: path
        required: true
        schema:
          type: string
    responses:
      200:
        description: A list of dealers for the product
        content:
          application/json:
            schema:
              type: object
              properties:
                dealers:
                  type: array
                  items:
                    type: string
      404:
        description: Product not found
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
    """
    product_obj = Product.query.filter_by(name=product).first()
    if product_obj:
        return jsonify({"dealers": product_obj.dealers})
    else:
        return jsonify({"message": f"Could not find dealers for {product}"}), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
