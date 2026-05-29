from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class ClienteBase(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: Optional[str] = None
    endereco: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True
