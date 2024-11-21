from fastapi import File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.Auth.Models.user_model import User
from app.Auth.Repository.auth_repository import AuthRepository
from app.Auth.Schemas.user_schema import UpdateUserSchema
import cv2
import face_recognition
import os



import uuid

class FacialDataService():
    def __init__(self, db: Session):
        self.auth_repo = AuthRepository(db)
        self.db = db

    def recognize(self, img):
        # Obtener los embeddings de la imagen desconocida
        embeddings_unknown = face_recognition.face_encodings(img)
        if len(embeddings_unknown) == 0:
            return 'no_persons_found', False
        else:
            embeddings_unknown = embeddings_unknown[0]

        # Buscar en la base de datos los embeddings de cada usuario
        match = False
        user_found = None

        users = self.auth_repo.get_all()

        for user in users:
            embeddings_db = user.embeddings  # Obtener los embeddings almacenados en la base de datos
            if not embeddings_db:
                continue
            # Comparar los embeddings de la base de datos con los desconocidos
            match = face_recognition.compare_faces([embeddings_db], embeddings_unknown)[0]
            if match:
                user_found = user
                break

        if match:
            return user_found.name, True 
        else:
            return 'unknown_person', False

    async def verify_face(self, file: UploadFile = File(...)):

        file.filename = f"{uuid.uuid4()}.png"
        contents = await file.read()

        with open(file.filename, "wb") as f:
            f.write(contents)
            
        user_name, match_status = self.recognize(cv2.imread(file.filename))


        os.remove(file.filename)

        return {'user': user_name, 'match_status': match_status}

    async def register_embedding(self, user_id: str, file: UploadFile = File(...)):
        user = self.auth_repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        file.filename = f"{user_id}.png"
        contents = await file.read()

        with open(file.filename, "wb") as f:
            f.write(contents)

        embeddings = face_recognition.face_encodings(cv2.imread(file.filename))
        user.embeddings = embeddings[0].tolist()  # Convertir ndarray a lista
        self.db.commit()

        os.remove(file.filename)

        return {'registration_status': 200}
