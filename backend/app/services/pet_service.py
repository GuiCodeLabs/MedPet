from sqlalchemy.orm import Session
from app.repositories.pet_repository import PetRepository
from app.repositories.cliente_repository import ClienteRepository
from app.models.pet import Pet
from app.schemas.pet_schema import PetCreate, PetUpdate



class PetService:
    def __init__(self, db: Session):
        self.repository = PetRepository(db)
        self.cliente_repository = ClienteRepository(db)

    def get_by_id(self, pet_id: int):
        return self.repository.get_by_id(pet_id)

    def create(self, pet_in: PetCreate) -> Pet:
        # Validar se o tutor (Cliente) existe
        dono = self.cliente_repository.get_by_id(pet_in.cliente_id)
        if not dono:
            raise ValueError("O tutor (cliente_id) informado não existe.")

        db_pet = Pet(
            nome=pet_in.nome,
            especie=pet_in.especie,
            raca=pet_in.raca,
            idade=pet_in.idade,
            peso=pet_in.peso,
            cliente_id=pet_in.cliente_id,
        )
        return self.repository.create(db_pet)

    def list_all(self):
        return self.repository.list_all()

    def list_by_owner(self, cliente_id: int):
        return self.repository.list_by_owner(cliente_id)

    def update(self, pet_id: int, pet_in: PetUpdate):
        db_pet = self.repository.get_by_id(pet_id)
        if not db_pet:
            raise ValueError("Pet não encontrado.")
        
        if pet_in.cliente_id is not None and pet_in.cliente_id != db_pet.cliente_id:
            dono = self.cliente_repository.get_by_id(pet_in.cliente_id)
            
            if not dono:
                raise ValueError("O tutor (cliente_id) informado não existe.")
            
        update_data = pet_in.dict(exclude_unset=True)
        return self.repository.update(db_pet, update_data)
    
    def delete(self, pet_id: int):
        db_pet = self.repository.get_by_id(pet_id)
        if not db_pet:
            raise ValueError("Pet não encontrado.")
        
        return self.repository.delete(db_pet)
    
    