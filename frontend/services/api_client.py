import streamlit as st
import os
import time
import requests

BASE_URL = os.getenv("API_URL", "http://localhost:8000")

def init_mock_db():
    if "db_tutores" not in st.session_state:
        st.session_state["db_tutores"] = []
    if "db_pets" not in st.session_state:
        st.session_state["db_pets"] = []
    if "db_consultas" not in st.session_state:
        st.session_state["db_consultas"] = []

def login(email, senha):
    """Conecta diretamente com o endpoint de autenticação do backend real"""
    try:
        # Envia a requisição com as chaves "username" e "password" que o schema do backend espera
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={"username": email, "password": senha}
        )
        
        # Se os dados estiverem corretos no banco de dados (HTTP 200)
        if response.status_code == 200:
            dados_api = response.json()
            # Devolve os dados estruturados conforme o seu TokenResponse do backend
            return {
                "token": dados_api["access_token"],
                "perfil": dados_api["perfil"],
                "nome": dados_api["nome"]
            }
        
        # Se o backend recusar (E-mail inválido, senha errada ou usuário inativo)
        else:
            erro_detalhe = response.json().get("detail", "Erro ao autenticar.")
            st.error(erro_detalhe)
            return None
            
    except requests.exceptions.ConnectionError:
        st.error("Erro de conexão: Garanta que o backend FastAPI está rodando na porta 8000!")
        return None

def get_tutores():
    """Simula um GET /api/v1/tutores"""
    time.sleep(0.3)
    init_mock_db()
    return st.session_state["db_tutores"]

def create_tutor(dados):
    """Simula um POST /api/v1/tutores"""
    time.sleep(0.5)
    init_mock_db()
    novo_id = len(st.session_state["db_tutores"]) + 1
    dados["id"] = novo_id
    st.session_state["db_tutores"].append(dados)
    return dados

def get_pets():
    """Simula um GET /api/v1/pets"""
    time.sleep(0.3)
    init_mock_db()
    return st.session_state["db_pets"]

def create_pet(dados):
    """Simula um POST /api/v1/pets"""
    time.sleep(0.5)
    init_mock_db()
    novo_id = len(st.session_state["db_pets"]) + 1
    dados["id"] = novo_id
    st.session_state["db_pets"].append(dados)
    return dados

def get_consultas():
    """Simula um GET /api/v1/consultas"""
    time.sleep(0.3)
    init_mock_db()
    return st.session_state["db_consultas"]

def create_consulta(dados):
    """Simula um POST /api/v1/consultas"""
    time.sleep(0.5)
    init_mock_db()
    novo_id = len(st.session_state["db_consultas"]) + 1
    dados["id"] = novo_id
    st.session_state["db_consultas"].append(dados)
    return dados

def get_usuarios():
    """Simula um GET /api/v1/usuarios (Apenas Admin)"""
    time.sleep(0.4)
    return [
        {"id": 1, "nome": "Admin", "email": "admin@medpet.com", "perfil": "admin"}
    ]
