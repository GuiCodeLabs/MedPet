from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.pet_schema import PetCreate, PetResponse, PetUpdate
from app.services.pet_service import PetService

router = APIRouter(prefix="/pets", tags=["Pets"])


@router.post("/", response_model=PetResponse, status_code=status.HTTP_201_CREATED)
def criar_pet(pet_in: PetCreate, db: Session = Depends(get_db)):
    service = PetService(db)
    try:
        return service.create(pet_in)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=List[PetResponse])
def listar_pets(db: Session = Depends(get_db)):
    service = PetService(db)
    return service.list_all()


@router.get("/tutor/{cliente_id}", response_model=List[PetResponse])
def listar_pets_por_tutor(cliente_id: int, db: Session = Depends(get_db)):
    service = PetService(db)
    return service.list_by_owner(cliente_id)

@router.get("/{id}", response_model=PetResponse)
def obter_pet(id: int, db: Session = Depends(get_db)):
    service = PetService(db)
    pet = service.get_by_id(id)

    if not pet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet não encontrado.")
    
    return pet

@router.put("/{id}", response_model=PetResponse)
def atualizar_pet(id: int, pet_in: PetUpdate, db: Session = Depends(get_db)):
    service = PetService(db)
    try:
        return service.update(id, pet_in)
    except ValueError as e:
        status_code = status.HTTP_404_NOT_FOUND if "não encontrado" in str(e) else status.HTTP_400_BAD_REQUEST
        raise HTTPException(status_code=status_code, detail=str(e))

@router.delete("/{id}")    
def deletar_pet(id: int, db: Session = Depends(get_db)):
    service = PetService(db)
    try:
        service.delete(id)
        return None
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
