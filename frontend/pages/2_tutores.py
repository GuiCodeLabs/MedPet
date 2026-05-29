import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.validators import is_valid_cpf, is_valid_email, is_valid_phone
from components.ui import page_header, load_css
from services.api_client import get_tutores, create_tutor

st.set_page_config(page_title="Tutores - MedPet", page_icon="👥", layout="wide")
load_css()

if "logado" not in st.session_state or not st.session_state["logado"]:
    st.warning("Você precisa fazer login para acessar esta página.")
    st.stop()

page_header("Gerenciamento de Tutores", "Cadastre e gerencie os tutores dos pacientes da clínica.")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Cadastrar Novo Tutor")
    with st.form("form_tutor"):
        nome = st.text_input("Nome Completo")
        cpf = st.text_input("CPF")
        email = st.text_input("E-mail")
        telefone = st.text_input("Telefone")
        
        submit = st.form_submit_button("Salvar Tutor", type="primary", width="stretch")
        if submit:
            erros = []
            if not nome:
                erros.append("O nome é obrigatório.")
            if not cpf or not is_valid_cpf(cpf):
                erros.append("CPF inválido. Certifique-se de digitar 11 dígitos.")
            if email and not is_valid_email(email):
                erros.append("E-mail inválido.")
            if telefone and not is_valid_phone(telefone):
                erros.append("Telefone inválido. Insira o DDD.")

            if not erros:
                create_tutor({
                    "nome": nome,
                    "cpf": cpf,
                    "email": email,
                    "telefone": telefone
                })
                st.success(f"Tutor {nome} cadastrado com sucesso!")
                st.rerun()
            else:
                for erro in erros:
                    st.error(erro)

with col2:
    st.subheader("Tutores Cadastrados")
    tutores = get_tutores()
    if tutores:
        df = pd.DataFrame(tutores)
        st.dataframe(df, width="stretch", hide_index=True)
    else:
        st.info("Nenhum tutor cadastrado.")
