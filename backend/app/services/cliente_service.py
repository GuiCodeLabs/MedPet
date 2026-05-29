from sqlalchemy.orm import Session
from app.repositories.cliente_repository import ClienteRepository
from app.models.cliente import Cliente
from app.schemas.cliente_schema import ClienteCreate, ClienteUpdate

class ClienteService:
    def __init__(self, db: Session):
        self.repository = ClienteRepository(db)

    def get_by_id(self, cliente_id: int):
        return self.repository.get_by_id(cliente_id)

    def update(self, cliente_id: int, cliente_in: ClienteUpdate) -> Cliente:
        cliente = self.repository.get_by_id(cliente_id)
        if not cliente:
            raise ValueError("Cliente não encontrado.")

        updated_data = cliente_in.dict(exclude_unset=True)

        return self.repository.update(cliente, updated_data)
    
    def delete(self, cliente_id: int):
        cliente = self.repository.get_by_id(cliente_id)
        if not cliente:
            raise ValueError("Cliente não encontrado.")

        self.repository.delete(cliente)

    def create(self, cliente_in: ClienteCreate) -> Cliente:
        # Validar CPF único
        existing_cpf = self.repository.get_by_cpf(cliente_in.cpf)
        if existing_cpf:
            raise ValueError("Cliente com este CPF já cadastrado.")

        # Validar E-mail único
        existing_email = self.repository.get_by_email(cliente_in.email)
        if existing_email:
            raise ValueError("Cliente com este E-mail já cadastrado.")

        db_cliente = Cliente(
            nome=cliente_in.nome,
            cpf=cliente_in.cpf,
            email=cliente_in.email,
            telefone=cliente_in.telefone,
            endereco=cliente_in.endereco
        )
        return self.repository.create(db_cliente)

    def list_all(self):
        return self.repository.list_all()
