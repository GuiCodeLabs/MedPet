import streamlit as st
import os
import requests

BASE_URL = os.getenv("API_URL", "http://localhost:8000")

def login(email, senha):
    """Conecta diretamente com o endpoint de autenticação do backend real"""
    try:
        # Envia a requisição com as chaves "username" e "password" que o schema do backend espera
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={"username": email, "password": senha},
            timeout=5
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
            
    except requests.exceptions.RequestException:
        st.error("Erro de conexão: Garanta que o backend FastAPI está rodando na porta 8000!")
        return None

@st.cache_data(ttl=30)
def get_tutores():
    try:
        response = requests.get(f"{BASE_URL}/clientes/", timeout=5)
        return response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        return []

def create_tutor(dados):
    try:
        response = requests.post(f"{BASE_URL}/clientes/", json=dados, timeout=5)
        if response.status_code == 201:
            st.cache_data.clear()
            return response.json()
        else:
            erro = response.json().get("detail", "Erro ao cadastrar tutor.")
            st.error(f"Erro: {erro}")
            return None
    except requests.exceptions.RequestException:
        st.error("Erro ao conectar com a API.")
        return None

@st.cache_data(ttl=30)
def get_pets():
    try:
        response = requests.get(f"{BASE_URL}/pets/", timeout=5)
        if response.status_code == 200:
            pets = response.json()
            for pet in pets:
                # O Frontend espera "tutor_id", mas o backend retorna "cliente_id"
                pet["tutor_id"] = pet.pop("cliente_id", None)
            return pets
        return []
    except requests.exceptions.RequestException:
        return []

def create_pet(dados):
    try:
        payload = {
            "nome": dados["nome"],
            "especie": dados["especie"],
            "raca": dados.get("raca", ""),
            "idade": dados.get("idade"),
            "peso": dados.get("peso"),
            "cliente_id": dados["tutor_id"]
        }
        response = requests.post(f"{BASE_URL}/pets/", json=payload, timeout=5)
        if response.status_code == 201:
            st.cache_data.clear()
            return response.json()
        else:
            erro = response.json().get("detail", "Erro ao cadastrar pet.")
            st.error(f"Erro: {erro}")
            return None
    except requests.exceptions.RequestException:
        st.error("Erro ao conectar com a API.")
        return None

@st.cache_data(ttl=30)
def get_consultas():
    try:
        response = requests.get(f"{BASE_URL}/atendimentos/", timeout=5)
        if response.status_code == 200:
            consultas = response.json()
            
            # Buscar pets (utiliza o cache da função já existente) para mapear o nome na tabela
            pets = get_pets()
            pets_map = {p["id"]: p["nome"] for p in pets} if pets else {}
                
            for c in consultas:
                c["pet"] = pets_map.get(c["pet_id"], "Desconhecido")
            return consultas
        return []
    except requests.exceptions.RequestException:
        return []

def create_consulta(dados):
    """POST /atendimentos/ - Criar nova consulta"""
    try:
        payload = {
            "motivo": dados["motivo"],
            "descricao": dados.get("descricao", ""),
            "pet_id": dados["pet_id"]
        }
        # Enviar data agendada se fornecida
        if dados.get("data"):
            payload["data"] = dados["data"]
        # Enviar status se fornecido
        if dados.get("status"):
            payload["status"] = dados["status"]
        response = requests.post(f"{BASE_URL}/atendimentos/", json=payload, timeout=5)
        if response.status_code == 201:
            st.cache_data.clear()
            return response.json()
        else:
            erro = response.json().get("detail", "Erro ao agendar consulta.")
            st.error(f"Erro: {erro}")
            return None
    except requests.exceptions.RequestException:
        st.error("Erro ao conectar com a API.")
        return None

def update_consulta(consulta_id, dados):
    """PUT /atendimentos/{id} - Atualizar consulta existente"""
    try:
        response = requests.put(f"{BASE_URL}/atendimentos/{consulta_id}", json=dados, timeout=5)
        if response.status_code == 200:
            st.cache_data.clear()
            return response.json()
        else:
            erro = response.json().get("detail", "Erro ao atualizar consulta.")
            st.error(f"Erro: {erro}")
            return None
    except requests.exceptions.RequestException:
        st.error("Erro ao conectar com a API.")
        return None

def get_usuarios():
    try:
        response = requests.get(f"{BASE_URL}/usuarios/", timeout=5)
        return response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        return []

def create_usuario(dados):
    """Cria um novo usuário no banco de dados via POST /usuarios/"""
    try:
        payload = {
            "nome": dados["nome"],
            "email": dados["email"],
            "perfil": dados.get("perfil", "atendente"),
            "senha": dados["senha"]
        }
        response = requests.post(f"{BASE_URL}/usuarios/", json=payload, timeout=5)
        if response.status_code == 201:
            st.cache_data.clear()
            return response.json()
        else:
            erro = response.json().get("detail", "Erro ao cadastrar usuário.")
            st.error(f"Erro: {erro}")
            return None
    except requests.exceptions.RequestException:
        st.error("Erro ao conectar com a API.")
        return None
