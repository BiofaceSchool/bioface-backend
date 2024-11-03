from http import HTTPStatus
import logging
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.Auth.Schemas.login_schema import TokenInfo
from app.Auth.Validators.token_validators import validate_jwt_token
from app.shared.Validator.error_factory import ValidationError


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)


    async def dispatch(self, request: Request, call_next) -> Response:
        excluded_routes = [
            "/api/v1/auth/login",
            "/api/v1/auth/register",
            "/docs",
            "/docs/",
            "/openapi.json"
        ]

        # Log para verificar si la ruta es excluida
        if request.url.path.startswith(tuple(excluded_routes)):
            logging.info(f"Accessing excluded route: {request.url.path}")
            return await call_next(request)
        
        
        token = request.cookies.get("access_token")
        try:
            payload = validate_jwt_token(token)
            request.state.user = payload
            return await call_next(request)
        except ValidationError as e:
            return JSONResponse(content={"detail": str(e)}, status_code=e.code)  # Usa el código de estado de la excepción
        except Exception as e:
            return JSONResponse(content={"detail": "Internal Server Error"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
     

