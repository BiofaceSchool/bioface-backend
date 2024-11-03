from fastapi import FastAPI, HTTPException
from app.Auth.Middlewares.auth_middleware import AuthMiddleware
from config.dependency_config import create_all_tables
from app.routes import routes
app = FastAPI()


try:
    create_all_tables()
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error al crear tablas: {e}")

app.include_router(routes)

app.add_middleware(AuthMiddleware)
