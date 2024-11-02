from fastapi import FastAPI
from .config.dependency_config import create_all_tables

app = FastAPI()


create_all_tables()
@app.get("/")
def index():
    return "hola mamawuebo"