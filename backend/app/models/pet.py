from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    especie = Column(String(30), nullable=False)  # Ex: Cachorro, Gato
    raca = Column(String(50), nullable=True)
    idade = Column(Integer, nullable=True)
    peso = Column(Float, nullable=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamento de volta para o tutor (Cliente)
    dono = relationship("Cliente", back_populates="pets")

    # Relacionamento de um pet para muitos atendimentos
    atendimentos = relationship(
        "Atendimento", back_populates="pet", cascade="all, delete-orphan"
    )
