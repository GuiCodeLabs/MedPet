from sqlalchemy.orm import Session
from app.repositories.atendimento_repository import AtendimentoRepository
from app.repositories.pet_repository import PetRepository
from app.models.atendimento import Atendimento
from app.schemas.atendimento_schema import AtendimentoCreate, AtendimentoUpdate


class AtendimentoService:
    def __init__(self, db: Session):
        self.repository = AtendimentoRepository(db)
        self.pet_repository = PetRepository(db)

    def get_by_id(self, atendimento_id: int):
        return self.repository.get_by_id(atendimento_id)

    def create(self, atendimento_in: AtendimentoCreate) -> Atendimento:
        # Validar se o pet existe
        pet = self.pet_repository.get_by_id(atendimento_in.pet_id)
        if not pet:
            raise ValueError("O pet (pet_id) informado não existe.")

        db_atendimento = Atendimento(
            motivo=atendimento_in.motivo,
            descricao=atendimento_in.descricao,
            pet_id=atendimento_in.pet_id,
        )
        # Atribuir data e status se fornecidos na requisição
        if atendimento_in.data is not None:
            db_atendimento.data = atendimento_in.data
        if atendimento_in.status is not None:
            db_atendimento.status = atendimento_in.status
        return self.repository.create(db_atendimento)

    def list_all(self):
        return self.repository.list_all()

    def list_by_pet(self, pet_id: int):
        return self.repository.list_by_pet(pet_id)

    def update(self, atendimento_id: int, atendimento_in: AtendimentoUpdate) -> Atendimento:
        # Validar se o atendimento existe
        atendimento = self.repository.get_by_id(atendimento_id)
        if not atendimento:
            raise ValueError("Atendimento não encontrado.")
        
        # Validar se o novo pet_id existe (se foi informado)
        if atendimento_in.pet_id and atendimento_in.pet_id != atendimento.pet_id:
            pet = self.pet_repository.get_by_id(atendimento_in.pet_id)
            if not pet:
                raise ValueError("O pet (pet_id) informado não existe.")
        
        # Preparar dados para atualização (apenas campos não-nulos)
        update_data = {}
        if atendimento_in.motivo is not None:
            update_data["motivo"] = atendimento_in.motivo
        if atendimento_in.descricao is not None:
            update_data["descricao"] = atendimento_in.descricao
        if atendimento_in.pet_id is not None:
            update_data["pet_id"] = atendimento_in.pet_id
        if atendimento_in.data is not None:
            update_data["data"] = atendimento_in.data
        if atendimento_in.status is not None:
            update_data["status"] = atendimento_in.status
        
        return self.repository.update(atendimento_id, update_data)

    def delete(self, atendimento_id: int) -> bool:
        # Validar se o atendimento existe
        atendimento = self.repository.get_by_id(atendimento_id)
        if not atendimento:
            raise ValueError("Atendimento não encontrado.")
        
        return self.repository.delete(atendimento_id)
