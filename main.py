import os
from fastapi import FastAPI, HTTPException
import uvicorn
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Usa el puerto de entorno o 8000 si no está definido
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)