from pydantic import BaseModel, ValidationError, Field
from typing import Optional
from datetime import datetime
from typing import List


class Pricing(BaseModel):
    amount: float
    currency: str

class Availability(BaseModel):
    quantity: int
    timestamp: str

class ProdutoTransform(BaseModel):
    id: str
    name: str
    description: str
    pricing: Pricing
    availability: Availability
    category: str

    class Config:
        schema_extra = {
            "example": {
                "id": "12345",
                "name": "Nome do Produto",
                "description": "Descrição do Produto",
                "pricing": {
                    "amount": 100.0,
                    "currency": "BRL"
                },
                "availability": {
                    "quantity": 50,
                    "timestamp": "2024-06-12T12:00:00Z"
                },
                "category": "Categoria do Produto"
            }
        }


class ProdutoManual(BaseModel):
    productId: str
    productName: str
    productDescription: str
    price: float
    currency: str
    stockQuantity: int
    category: str
    
    class Config:
        schema_extra = {
            "example": {
                "productId": "12345",
                "productName": "Nome do Produto",
                "productDescription": "Descrição do Produto",
                "price": 100.0,
                "currency": "BRL",
                "stockQuantity": 50,
                "category": "Categoria do Produto"
            }
        }