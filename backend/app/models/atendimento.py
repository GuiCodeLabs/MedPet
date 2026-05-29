from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, index=True)
    motivo = Column(String(100), nullable=False)  # Ex: Consulta, Vacina, Cirurgia
    descricao = Column(String(500), nullable=True)  # Observações clínicas
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    data = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamento de volta para o pet atendido
    pet = relationship("Pet", back_populates="atendimentos")
