# app/services/usuario_service.py
from sqlalchemy.orm import Session
from app.repositories.usuario_repository import UsuarioRepository
from app.models.usuario import Usuario
from app.schemas.usuario_schema import UsuarioCreate
from app.schemas.auth_schema import LoginRequest, TokenResponse
from app.core.security import get_password_hash, verify_password, create_access_token


class UsuarioService:
    def __init__(self, db: Session):
        self.repository = UsuarioRepository(db)

    def create(self, user_in: UsuarioCreate) -> Usuario:
        existing = self.repository.get_by_email(user_in.email)
        if existing:
            raise ValueError("Um usuário com este e-mail já existe.")

        hashed_password = get_password_hash(user_in.senha)

        db_user = Usuario(
            nome=user_in.nome,
            email=user_in.email,
            senha_hash=hashed_password,
            perfil=user_in.perfil,
            ativo=user_in.ativo,
        )
        return self.repository.create(db_user)

    def autenticar_usuario(self, login_data: LoginRequest) -> TokenResponse:
        usuario = self.repository.get_by_email(login_data.email)
        if not usuario:
            raise ValueError("E-mail ou senha incorretos.")

        if not usuario.ativo:
            raise ValueError("Usuário inativo no sistema.")

        if not verify_password(login_data.senha, usuario.senha_hash):
            raise ValueError("E-mail ou senha incorretos.")

        token_data = {"sub": usuario.email, "perfil": usuario.perfil}
        access_token = create_access_token(data=token_data)

        return TokenResponse(
            access_token=access_token, perfil=usuario.perfil, nome=usuario.nome
        )

    def list_all(self):
        return self.repository.list_all()
