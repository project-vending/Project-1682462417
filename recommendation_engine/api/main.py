python
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API for the Recommendation Engine!"}

@app.get("/recommend")
def recommend():
    # Implement the recommendation engine logic here
    recommendations = {"products": ["Product 1", "Product 2", "Product 3"]}
    return json.dumps(recommendations)
