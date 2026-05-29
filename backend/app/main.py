# app/main.py
from fastapi import FastAPI
from app.database import Base, engine, get_db
from app.routes import usuario_routes, auth_routes
from app.models import usuario, cliente, pet, atendimento
from app.repositories.usuario_repository import UsuarioRepository
from app.core.security import get_password_hash
from app.models.usuario import Usuario

app = FastAPI(title="MEDPET - Clínica Veterinária")

# Cria as tabelas do banco
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def criar_admin_padrao():
    db = next(get_db())
    repository = UsuarioRepository(db)
    
    # Verifica se já existe QUALQUER usuário cadastrado
    if not repository.list_all():
        print("Instanciando administrador inicial do sistema...")
        admin_usuario = Usuario(
            nome="Administrador MedPet",
            email="admin@medpet.com",
            senha_hash=get_password_hash("admin123"), # Senha inicial padrão
            perfil="admin",
            ativo=True
        )
        repository.create(admin_usuario)
        print("Administrador padrão (admin@medpet.com / admin123) criado com sucesso!")

app.include_router(usuario_routes.router)
app.include_router(auth_routes.router)

@app.get("/")
def home():
    return {"mensagem": "API MEDPET funcionando!"}