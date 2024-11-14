from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session


from app.University.Schemas.university_schema import UniversityDetailResponse, UniversityRequest, UniversityResponse
from config.dependency_config import get_db

from ..Services.university_service import UniversityService

university = APIRouter()

@university.post('/add', status_code=status.HTTP_201_CREATED)
def add_university(request: UniversityRequest, db: Session = Depends(get_db)):
    university_service = UniversityService(db)
    response = university_service.add_university(request)
    return response

@university.get('/get_all', status_code=status.HTTP_200_OK, response_model=list[UniversityResponse])
def get_all_universities(db: Session = Depends(get_db)):
    university_service = UniversityService(db)
    response = university_service.get_all_universities()
    return response

@university.get('/get_campuses/{university_id}', status_code=status.HTTP_200_OK, response_model=UniversityDetailResponse) 
def get_university_campuses(university_id: int, db: Session = Depends(get_db)):
    try:
        university_service = UniversityService(db)
        response = university_service.get_university_campuses(university_id)
        return response
    except Exception as e:
        return {"message": {"error": str(e)}}
    
@university.get('/get/{id}', status_code=status.HTTP_200_OK)
def get_university_by_id(id: int, db: Session = Depends(get_db)):
    university_service = UniversityService(db)
    response = university_service.get_university_by_id(id)
    return response

@university.get('/get_by_name/{name}', status_code=status.HTTP_200_OK)
def get_university_by_name(name: str, db: Session = Depends(get_db)):
    university_service = UniversityService(db)
    response = university_service.get_by_name(name)
    return response


@university.put('/update/{id}', status_code=status.HTTP_200_OK)
def update_university(request: UniversityRequest, id: int, db: Session = Depends(get_db)):
    university_service = UniversityService(db)
    response = university_service.update_university(request, id)
    return response


@university.delete('/delete/{id}', status_code=status.HTTP_200_OK)
def delete_university(id: int, db: Session = Depends(get_db)):
    university_service = UniversityService(db)
    response = university_service.delete_university(id)
    return response
