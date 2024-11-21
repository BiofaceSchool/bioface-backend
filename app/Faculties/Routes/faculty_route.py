from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session


from app.Faculties.Schemas.faculty_schema import FacultyRequest, FacultyResponse

from app.Faculties.Services.faculty_service import FacultyService
from config.dependency_config import get_db
from typing import List


faculty = APIRouter()

@faculty.post('/add', status_code=status.HTTP_201_CREATED)
def add_faculty(request: FacultyRequest, campus_id: int, db: Session = Depends(get_db)):
    try: 
        faculty_service = FacultyService(db)
        response = faculty_service.add_faculty(request, campus_id)
        return response
    except Exception as e:
        return {"message": {"error": str(e)}}

@faculty.get('/get-all', response_model=List[FacultyResponse])
def get_all_faculties(db: Session = Depends(get_db)):
    faculty_service = FacultyService(db)
    response = faculty_service.get_all_faculties()
    return response

@faculty.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=FacultyResponse)
def get_faculty_by_id(id: int, db: Session = Depends(get_db)):
    faculty_service = FacultyService(db)
    response = faculty_service.get_faculty_by_id(id)
    return response

@faculty.put('/update/{id}', status_code=status.HTTP_200_OK)
def update_faculty(request: FacultyRequest, id: int, db: Session = Depends(get_db)):
    faculty_service = FacultyService(db)
    response = faculty_service.update_faculty(request, id)
    return response

@faculty.delete('/delete/{id}', status_code=status.HTTP_200_OK)
def delete_faculty(id: int, db: Session = Depends(get_db)):
    faculty_service = FacultyService(db)
    response = faculty_service.delete_faculty(id)
    return response


