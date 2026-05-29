from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.cliente_schema import ClienteCreate, ClienteResponse
from app.services.cliente_service import ClienteService

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.post("/", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente_in: ClienteCreate, db: Session = Depends(get_db)):
    service = ClienteService(db)
    try:
        return service.create(cliente_in)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    service = ClienteService(db)
    return service.list_all()

@router.get("/{id}", response_model=ClienteResponse)
def obter_cliente(id: int, db: Session = Depends(get_db)):
    service = ClienteService(db)
    cliente = service.get_by_id(id)
    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado.")
    return cliente
