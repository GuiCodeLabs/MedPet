import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.ui import page_header, load_css
from services.api_client import get_usuarios, create_usuario

st.set_page_config(page_title="Usuários - MedPet", page_icon="🔐", layout="wide")
load_css()

if "logado" not in st.session_state or not st.session_state["logado"]:
    st.warning("Você precisa fazer login para acessar esta página.")
    st.stop()

if st.session_state.get("perfil") != "admin":
    st.error("Acesso negado. Apenas administradores podem ver esta página.")
    st.stop()

page_header("Gerenciamento de Usuários", "Área restrita para administradores do sistema.")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Novo Usuário")
    with st.form("form_user"):
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        perfil = st.selectbox("Perfil", ["user", "admin"])
        senha = st.text_input("Senha", type="password")
        
        submit = st.form_submit_button("Cadastrar", type="primary", width="stretch")
        if submit:
            # Validação dos campos obrigatórios
            if not nome or not email or not senha:
                st.error("Preencha todos os campos obrigatórios (Nome, E-mail e Senha).")
            else:
                resultado = create_usuario({
                    "nome": nome,
                    "email": email,
                    "perfil": perfil,
                    "senha": senha
                })
                if resultado:
                    st.success(f"Usuário '{nome}' cadastrado com sucesso!")
                    st.rerun()

with col2:
    st.subheader("Usuários Ativos")
    users = get_usuarios()
    if users:
        df = pd.DataFrame(users)
        # Remover colunas sensíveis da exibição se existirem
        colunas_exibir = [c for c in df.columns if c not in ["senha", "password"]]
        st.dataframe(df[colunas_exibir], width="stretch", hide_index=True)
    else:
        st.info("Nenhum usuário cadastrado ainda.")
