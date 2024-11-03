# app/config/main_router.py
from fastapi import APIRouter
from app.shared.config.routes_config import *

from app.Auth.Routes.auth_route import auth

routes = APIRouter()

# AUTH ROUTES
routes.include_router(auth, prefix=AUTH_ROUTE, tags=[AUTH_TAG])

