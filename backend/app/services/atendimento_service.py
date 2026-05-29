from sqlalchemy.orm import Session
from app.repositories.atendimento_repository import AtendimentoRepository
from app.repositories.pet_repository import PetRepository
from app.models.atendimento import Atendimento
from app.schemas.atendimento_schema import AtendimentoCreate


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
        return self.repository.create(db_atendimento)

    def list_all(self):
        return self.repository.list_all()

    def list_by_pet(self, pet_id: int):
        return self.repository.list_by_pet(pet_id)
