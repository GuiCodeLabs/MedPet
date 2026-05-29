from sqlalchemy.orm import Session
from app.models.cliente import Cliente

class ClienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, cliente_id: int):
        return self.db.query(Cliente).filter(Cliente.id == cliente_id).first()

    def get_by_cpf(self, cpf: str):
        return self.db.query(Cliente).filter(Cliente.cpf == cpf).first()

    def get_by_email(self, email: str):
        return self.db.query(Cliente).filter(Cliente.email == email).first()

    def create(self, cliente: Cliente):
        self.db.add(cliente)
        self.db.commit()
        self.db.refresh(cliente)
        return cliente

    def list_all(self):
        return self.db.query(Cliente).all()
