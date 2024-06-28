from fastapi import FastAPI
from scheduler.consumer import start_consumer

app = FastAPI()

@app.on_event("startup")
def startup_event():
    start_consumer()

@app.get("/")
def read_root():
    return {"message": "FastAPI Kafka Consumer is running"}