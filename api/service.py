from api.model import ProdutoDB
from api.schema import  ProdutoTransform
from .producer import produce_message
from api.db import session, new_session


class ApiService:
    
    def __init__(self):
        self.db = session
        
    
    def cadastroProduto(self, produto: ProdutoTransform):
        session = new_session()
        db_produto = ProdutoDB(
            productId=produto.id,
            productName=produto.name,
            productDescription=produto.description,
            price=produto.pricing.amount,
            currency=produto.pricing.currency,
            stockQuantity=produto.availability.quantity,
            category=produto.category,
            timestamp=produto.availability.timestamp,
            request_payload=produto.json(),
            response_payload=None, 
        )
        session.add(db_produto)
        session.commit()
        session.refresh(db_produto)
        return db_produto