from sqlalchemy.orm import Session
from app.repositories.usuario_repository import UsuarioRepository
from app.core.security import verify_password, create_access_token
from app.schemas.auth_schema import LoginRequest, TokenResponse

class AuthService:
    def __init__(self, db: Session):
        self.repository = UsuarioRepository(db)

    def authenticate_user(self, login_data: LoginRequest) -> TokenResponse:
        user = self.repository.get_by_email(login_data.username)
        if not user:
            return None
        
        if not verify_password(login_data.password, user.senha_hash):
            return None

        # Gerar o token de acesso JWT
        token_data = {"sub": user.email, "perfil": user.perfil}
        access_token = create_access_token(data=token_data)

        return TokenResponse(
            access_token=access_token,
            token_type="bearer"
        )
