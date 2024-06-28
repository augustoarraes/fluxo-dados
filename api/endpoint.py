from fastapi import FastAPI, HTTPException
from api.schema import ProdutoTransform, ProdutoManual
from api.service import ApiService
from api.producer import produce_message

app = FastAPI(title='Fluxo-Dados APP', description='API do Fluxo-Dados, by Augusto Arraes')

apiService = ApiService()


@app.post("/produto/scheduler", response_model=ProdutoTransform)
def create_product(produto: ProdutoTransform):
    item_produto = apiService.cadastroProduto(produto)
    product_message = item_produto.to_dict()
    produce_message('produtos-persistidos', product_message)
    return product_message


@app.post("/produto/manual")
def create_product(produto: ProdutoManual):
    try:
        product_message = produto.json()
        produce_message('cadastro-produtos', product_message)
        return {"message": "Product message sent to Kafka", "product": produto}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

