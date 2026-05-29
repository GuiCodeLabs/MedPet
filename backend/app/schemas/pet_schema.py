from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PetBase(BaseModel):
    nome: str
    especie: str
    raca: Optional[str] = None
    idade: Optional[int] = None
    peso: Optional[float] = None
    cliente_id: int


class PetCreate(PetBase):
    pass


class PetResponse(PetBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True

class PetUpdate(BaseModel):
    nome: Optional[str] = None
    especie: Optional[str] = None
    raca: Optional[str] = None
    idade: Optional[int] = None
    peso: Optional[float] = None
    cliente_id: Optional[int] = None
