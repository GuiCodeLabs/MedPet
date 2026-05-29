from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, index=True, nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    telefone = Column(String(20), nullable=True)
    endereco = Column(String(200), nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamento de um cliente para muitos pets
    pets = relationship("Pet", back_populates="dono", cascade="all, delete-orphan")
