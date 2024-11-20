from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session

from app.Campus.Schemas.campus_schema import CampusRequest, CampusResponse
from app.Campus.Services.campus_service import CampusService
from app.Faculties.Schemas.faculty_schema import FacultyResponse
from config.dependency_config import get_db


campus = APIRouter()

@campus.post('/add', status_code=status.HTTP_201_CREATED)
def add_campus(request: CampusRequest, university_id: int, db: Session = Depends(get_db)):
    campus_service = CampusService(db)
    response = campus_service.add_campus(request, university_id)
    return response

@campus.get('/get-all', response_model=list[CampusResponse])
def get_all_campuses(db: Session = Depends(get_db)):
    campus_service = CampusService(db)
    response = campus_service.get_all_campuses()
    return response


@campus.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=CampusResponse)
def get_campus_by_id(id: int, db: Session = Depends(get_db)):
    campus_service = CampusService(db)
    response = campus_service.get_campus_by_id(id)
    return response

@campus.put('/update/{id}', status_code=status.HTTP_200_OK)
def update_campus(request: CampusRequest, id: int, db: Session = Depends(get_db)):
    campus_service = CampusService(db)
    response = campus_service.update_campus(request, id)
    return response

@campus.delete('/delete/{id}', status_code=status.HTTP_200_OK)
def delete_campus(id: int, db: Session = Depends(get_db)):
    campus_service = CampusService(db)
    response = campus_service.delete_campus(id)
    return response

@campus.get('/get-faculties/{campus_id}', status_code=status.HTTP_200_OK, response_model=list[FacultyResponse])
def get_faculties_by_campus(campus_id: int, db: Session = Depends(get_db)):
    campus_service = CampusService(db)
    response = campus_service.get_faculties_by_campus(campus_id)
    return response
