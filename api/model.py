from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import Mapped
from api.db import engine

Base = declarative_base()

class ProdutoDB(Base):
    __tablename__ = 'products'
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    productId: Mapped[str] = Column(String, nullable=False)
    productName: Mapped[str] = Column(String, nullable=False)
    productDescription: Mapped[str] = Column(Text, nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    currency: Mapped[str] = Column(String, nullable=False)
    stockQuantity: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[str] = Column(String, nullable=False)
    timestamp: Mapped[str] = Column(String, nullable=False)
    request_payload: Mapped[str] = Column(Text, nullable=True)
    response_payload: Mapped[str] = Column(Text, nullable=True)
    created: Mapped[datetime] = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated: Mapped[datetime] = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted: Mapped[bool] = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<Product(productId='{self.productId}', productName='{self.productName}', price={self.price}, stockQuantity={self.stockQuantity})>"
    
    def to_dict(self):
        return {
            "id": self.productId,
            "name": self.productName,
            "description": self.productDescription,
            "pricing": {
                "amount": self.price,
                "currency": self.currency
            },
            "availability": {
                "quantity": self.stockQuantity,
                "timestamp": str(self.timestamp)
            },
            "category": self.category
        }


Base.metadata.create_all(bind=engine)