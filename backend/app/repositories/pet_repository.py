from sqlalchemy.orm import Session
from app.models.pet import Pet


class PetRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, pet_id: int):
        return self.db.query(Pet).filter(Pet.id == pet_id).first()

    def create(self, pet: Pet):
        self.db.add(pet)
        self.db.commit()
        self.db.refresh(pet)
        return pet

    def list_all(self):
        return self.db.query(Pet).all()

    def list_by_owner(self, cliente_id: int):
        return self.db.query(Pet).filter(Pet.cliente_id == cliente_id).all()
