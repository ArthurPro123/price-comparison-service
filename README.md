
# Price Comparison Service

**Compare product prices from multiple dealers in one place.**

---

## What It Does
This project helps you find the best prices for products like laptops, headphones, and printers from different dealers. It consists of three microservices:
- **Product List**: View products and their dealers.
- **Dealer Details**: Get detailed dealer information.
- **Frontend**: User-friendly web interface to compare prices.

---

## How it Does It
- The frontend orchestrates the interaction between the two services.
- The **Product Service** provides the product list.
- The **Dealer Service** provides the the names of the dealers and their prices.

---

## How to Use
1. **Run the services** (see setup below).
2. **Browse products** at [http://localhost:5001](http://localhost:5001).
3. **Compare prices** and choose the best deal.

---

## Product Service API

This service provides endpoints to fetch products and their associated dealers.

### Base URL

- **Local:** `http://localhost:5000`

---

### Endpoints

#### 1. Get List of Products

**Endpoint:**
`GET /products`

**Description:**
Fetches a list of all available products and their dealers.

**Example Request:**
```bash
curl http://localhost:5000/products
```

**Example Response:**
```json
{
  "products": [
    {
      "product": "Headphones",
      "Dealers": ["Binglee", "DXC Electronics", "Bobay"]
    },
    {
      "product": "Laptop",
      "Dealers": ["GH Computers", "Tech City", "Ez PC"]
    }
  ]
}
```

#### 2. Get Dealers for a Specific Product

**Endpoint:**
`GET /getdealers/{product}`

**Description:**
Fetches the list of dealers for a specific product.

**Parameters:**

| Parameter | Type   | Description                |
|-----------|--------|----------------------------|
| `product` | string | Name of the product        |


**Example Request:**
```bash
curl http://localhost:5000/getdealers/Laptop
```

**Example Response:**
```json
{
  "dealers": ["GH Computers", "Tech City", "Ez PC"]
}
```

---

## Dealer Service API

This service provides endpoints to fetch product prices from various dealers.

### Base URL

- **Local:** `http://localhost:8080`

---

### Endpoints

#### 1. Get Price for a Specific Dealer and Product

**Endpoint:**
`GET /price/{dealer}/{product}`

**Description:**
Fetches the price of a specific product from a specific dealer.

**Parameters:**

| Parameter | Type   | Description                |
|-----------|--------|----------------------------|
| `dealer`  | string | Name of the dealer         |
| `product` | string | Name of the product        |

**Example Request:**
```bash
curl http://localhost:8080/price/Binglee/Headphones
```

**Example Response:**
```json
{
  "message":"Headphones costs $30 at Binglee"
}
```


#### 2. Get All Prices for a Product

**Endpoint:**
`GET /allprice/{product}`

**Description:**
Fetches the prices of a specific product from all available dealers.

**Parameters:**

| Parameter | Type   | Description         |
|-----------|--------|---------------------|
| `product` | string | Name of the product |

**Example Request:**
```bash
curl http://localhost:8080/allprice/Printer
```

**Example Response:**
```json
{
  "prices": [
    { "key": "Binglee", "value": "$75" },
    { "key": "DXC Electronics", "value": "$85" }
  ]
}
```

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
