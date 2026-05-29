from pydantic import BaseModel, EmailStr
from datetime import datetime


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    perfil: str = "atendente"
    ativo: bool = True


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioResponse(UsuarioBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True
