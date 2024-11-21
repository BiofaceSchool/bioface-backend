# app/config/main_router.py
from fastapi import APIRouter
from app.shared.config.routes_constants import *

from app.Auth.Routes.auth_route import auth
from app.University.Routes.university_route import university
from app.Faculties.Routes.faculty_route import faculty
from app.Campus.Routes.campus_route import campus
#from app.Camera.Routes.facial_data_route import facial_data
routes = APIRouter()

# AUTH ROUTES
routes.include_router(auth, prefix=AUTH_ROUTE, tags=[AUTH_TAG])

# UNIVERSITY ROUTES
routes.include_router(university, prefix=UNIVERSITY_ROUTE, tags=[UNIVERSITY_TAG])

# FACULTY ROUTES
routes.include_router(faculty, prefix=FACULTY_ROUTE, tags=[FACULTY_TAG])

# CAMPUS ROUTES
routes.include_router(campus, prefix=CAMPUS_ROUTE, tags=[CAMPUS_TAG])

# FACE ENCODING ROUTES
#routes.include_router(facial_data, prefix=FACE_ENCODING_ROUTE, tags=[FACE_ENCODING_TAG])

