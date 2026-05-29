from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.atendimento_schema import AtendimentoCreate, AtendimentoUpdate, AtendimentoResponse
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

@router.get("/{atendimento_id}", response_model=AtendimentoResponse)
def obter_atendimento(atendimento_id: int, db: Session = Depends(get_db)):
    service = AtendimentoService(db)
    atendimento = service.get_by_id(atendimento_id)
    if not atendimento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Atendimento não encontrado.")
    return atendimento

@router.put("/{atendimento_id}", response_model=AtendimentoResponse)
def atualizar_atendimento(atendimento_id: int, atendimento_in: AtendimentoUpdate, db: Session = Depends(get_db)):
    service = AtendimentoService(db)
    try:
        return service.update(atendimento_id, atendimento_in)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{atendimento_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_atendimento(atendimento_id: int, db: Session = Depends(get_db)):
    service = AtendimentoService(db)
    try:
        service.delete(atendimento_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
