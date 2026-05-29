from fastapi import FastAPI

from app.database import Base, engine
from app.routes import usuario_routes, auth_routes
from app.models import usuario, cliente, pet, atendimento

app = FastAPI(title="MEDPET - Clínica Veterinária")

Base.metadata.create_all(bind=engine)

app.include_router(usuario_routes.router)
app.include_router(auth_routes.router)


@app.get("/")
def home():
    return {"mensagem": "API MEDPET funcionando!"}