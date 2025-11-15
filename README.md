
# Price Comparison Service

**Compare product prices from multiple dealers in one place.**

---

## What It Does
This project helps you find the best prices for products like laptops, headphones, and printers from different dealers. It consists of three microservices:
- **Product List**: View products and their dealers.
- **Dealer Details**: Get detailed dealer information.
- **Frontend**: User-friendly web interface to compare prices.

---

## How to Use
1. **Run the services** (see setup below).
2. **Browse products** at [http://localhost:5001](http://localhost:5001).
3. **Compare prices** and choose the best deal.

---

## API Endpoints
- Get all products:
  ```bash
  curl http://localhost:5000/products
  ```
- Get dealers for a product:
  ```bash
  curl http://localhost:5000/getdealers/Laptop
  ```
- View OpenAPI specification:
  ```bash
  curl http://localhost:5000/apispec_1.json
  ```
- View API docs: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

---

## Frontend
The frontend is a simple web page that allows users to select a product and view prices from different dealers. It uses Axios to fetch data from the backend services and displays it in a table.

- **Features**:
  - Dropdown to select products.
  - Table to display dealer prices.
  - Responsive design for mobile and desktop.

---

## Setup
Each microservice (`backend__dealer_details`, `backend__products_list`, `frontend__dealer_evaluation`) has its own `Dockerfile`. Run them together using Docker Compose.

---

**Find the best deals, fast!** 🚀

---

The following repositories were used as the starting point for this project:
- [IBM Developer Skills Network: Dealer Evaluation Backend](https://github.com/ibm-developer-skills-network/dealer_evaluation_backend.git)
- [IBM Developer Skills Network: Dealer Evaluation Frontend](https://github.com/ibm-developer-skills-network/dealer_evaluation_frontend.git)
