from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.atendimento_schema import AtendimentoCreate, AtendimentoResponse
from app.services.atendimento_service import AtendimentoService

router = APIRouter(prefix="/atendimentos", tags=["Atendimentos"])


@router.post(
    "/", response_model=AtendimentoResponse, status_code=status.HTTP_201_CREATED
)
def criar_atendimento(atendimento_in: AtendimentoCreate, db: Session = Depends(get_db)):
    service = AtendimentoService(db)
    try:
        return service.create(atendimento_in)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=List[AtendimentoResponse])
def listar_atendimentos(db: Session = Depends(get_db)):
    service = AtendimentoService(db)
    return service.list_all()


@router.get("/pet/{pet_id}", response_model=List[AtendimentoResponse])
def listar_atendimentos_por_pet(pet_id: int, db: Session = Depends(get_db)):
    service = AtendimentoService(db)
    return service.list_by_pet(pet_id)
