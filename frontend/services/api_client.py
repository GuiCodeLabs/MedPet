import streamlit as st
import os
import time

BASE_URL = os.getenv("API_URL", "http://localhost:8000")

def init_mock_db():
    if "db_tutores" not in st.session_state:
        st.session_state["db_tutores"] = []
    if "db_pets" not in st.session_state:
        st.session_state["db_pets"] = []
    if "db_consultas" not in st.session_state:
        st.session_state["db_consultas"] = []

def login(email, senha):
    """Simula um POST /api/v1/auth/login"""
    time.sleep(0.6)  # Simula latência de rede
    if email == "admin@medpet.com" and senha == "admin":
        return {"token": "mock_token_123", "perfil": "admin", "nome": "Admin"}
    elif email and senha:
        return {"token": "mock_token_user", "perfil": "user", "nome": "Usuário"}
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
