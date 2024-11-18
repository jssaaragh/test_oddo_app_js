from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from odoo import api, fields, models, tools
import os
import odoo

app = FastAPI()

# Load Odoo configurations
def configure_odoo():
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '5432')
    db_user = os.getenv('DB_USER', 'odoo')
    db_password = os.getenv('DB_PASSWORD', 'odoo')

    odoo.tools.config['db_host'] = db_host
    odoo.tools.config['db_port'] = db_port
    odoo.tools.config['db_user'] = db_user
    odoo.tools.config['db_password'] = db_password

    # Initialize Odoo connection
    odoo.cli.main()

# Sample Odoo Model
class Product(models.Model):
    _name = 'product.product'
    _description = 'Product'

    name = fields.Char('Product Name', required=True)
    description = fields.Text('Product Description')
    price = fields.Float('Price')

# Pydantic models for request and response validation
class ProductIn(BaseModel):
    name: str
    description: str = None
    price: float = 0.0

class ProductOut(ProductIn):
    id: int

# CRUD Operations
@app.get("/products", response_model=list[ProductOut])
async def get_products():
    try:
        # Retrieve all products
        products = odoo.env['product.product'].search([])
        return [{"id": product.id, "name": product.name, "description": product.description, "price": product.price} for product in products]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/products", response_model=ProductOut)
async def create_product(product_in: ProductIn):
    try:
        # Create a new product
        product = odoo.env['product.product'].create({
            'name': product_in.name,
            'description': product_in.description or '',
            'price': product_in.price
        })
        return {"id": product.id, "name": product.name, "description": product.description, "price": product.price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/products/{id}", response_model=ProductOut)
async def update_product(id: int, product_in: ProductIn):
    try:
        product = odoo.env['product.product'].browse(id)
        if not product.exists():
            raise HTTPException(status_code=404, detail="Product not found")

        product.write({
            'name': product_in.name,
            'description': product_in.description or product.description,
            'price': product_in.price or product.price
        })
        return {"id": product.id, "name": product.name, "description": product.description, "price": product.price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/products/{id}")
async def delete_product(id: int):
    try:
        product = odoo.env['product.product'].browse(id)
        if not product.exists():
            raise HTTPException(status_code=404, detail="Product not found")

        product.unlink()
        return {"message": "Product deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    configure_odoo()
