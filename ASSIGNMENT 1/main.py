from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 50000, "stock": 10},
    {"id": 2, "name": "Shoes", "category": "fashion", "price": 2000, "stock": 0},
    {"id": 3, "name": "Phone", "category": "electronics", "price": 20000, "stock": 5}
]

@app.get("/products")
def get_products():
    return products


@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    return [p for p in products if p["category"] == category_name]


@app.get("/products/instock")
def get_instock_products():
    return [p for p in products if p["stock"] > 0]


@app.get("/store/summary")
def store_summary():
    total_products = len(products)
    total_stock = sum(p["stock"] for p in products)
    return {"total_products": total_products, "total_stock": total_stock}


@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    return [p for p in products if keyword.lower() in p["name"].lower()]


@app.get("/products/deals")
def product_deals():
    return [p for p in products if p["price"] < 3000]