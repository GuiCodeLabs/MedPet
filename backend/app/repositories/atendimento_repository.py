from sqlalchemy.orm import Session
from app.models.atendimento import Atendimento


class AtendimentoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, atendimento_id: int):
        return (
            self.db.query(Atendimento).filter(Atendimento.id == atendimento_id).first()
        )

    def create(self, atendimento: Atendimento):
        self.db.add(atendimento)
        self.db.commit()
        self.db.refresh(atendimento)
        return atendimento

    def list_all(self):
        return self.db.query(Atendimento).all()

    def list_by_pet(self, pet_id: int):
        return self.db.query(Atendimento).filter(Atendimento.pet_id == pet_id).all()

    def update(self, atendimento_id: int, atendimento_data: dict):
        atendimento = self.db.query(Atendimento).filter(Atendimento.id == atendimento_id).first()
        if atendimento:
            for key, value in atendimento_data.items():
                if value is not None:
                    setattr(atendimento, key, value)
            self.db.commit()
            self.db.refresh(atendimento)
        return atendimento

    def delete(self, atendimento_id: int):
        atendimento = self.db.query(Atendimento).filter(Atendimento.id == atendimento_id).first()
        if atendimento:
            self.db.delete(atendimento)
            self.db.commit()
            return True
        return False
