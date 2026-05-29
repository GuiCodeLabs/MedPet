from sqlalchemy.orm import Session
from app.repositories.usuario_repository import UsuarioRepository
from app.models.usuario import Usuario
from app.schemas.usuario_schema import UsuarioCreate
from app.core.security import get_password_hash

class UsuarioService:
    def __init__(self, db: Session):
        self.repository = UsuarioRepository(db)

    def get_by_email(self, email: str):
        return self.repository.get_by_email(email)

    def create(self, user_in: UsuarioCreate) -> Usuario:
        # Verificar se já existe um usuário com o mesmo e-mail
        existing = self.repository.get_by_email(user_in.email)
        if existing:
            raise ValueError("Um usuário com este e-mail já existe.")

        # Hash da senha antes de persistir
        hashed_password = get_password_hash(user_in.senha)

        db_user = Usuario(
            nome=user_in.nome,
            email=user_in.email,
            senha_hash=hashed_password,
            perfil=user_in.perfil,
            ativo=user_in.ativo
        )
        return self.repository.create(db_user)

    def list_all(self):
        return self.repository.list_all()
