from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AtendimentoBase(BaseModel):
    motivo: str
    descricao: Optional[str] = None
    pet_id: int


class AtendimentoCreate(AtendimentoBase):
    data: Optional[datetime] = None
    status: Optional[str] = "Agendada"


class AtendimentoUpdate(BaseModel):
    motivo: Optional[str] = None
    descricao: Optional[str] = None
    pet_id: Optional[int] = None
    data: Optional[datetime] = None
    status: Optional[str] = None


class AtendimentoResponse(AtendimentoBase):
    id: int
    data: datetime
    status: Optional[str] = None

    class Config:
        from_attributes = True
