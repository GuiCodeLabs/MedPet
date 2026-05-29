from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AtendimentoBase(BaseModel):
    motivo: str
    descricao: Optional[str] = None
    pet_id: int


class AtendimentoCreate(AtendimentoBase):
    pass


class AtendimentoResponse(AtendimentoBase):
    id: int
    data: datetime

    class Config:
        from_attributes = True
