import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.ui import page_header, load_css
from services.api_client import get_pets, get_tutores, create_pet

st.set_page_config(page_title="Pets - MedPet", page_icon="🐾", layout="wide")
load_css()

if "logado" not in st.session_state or not st.session_state["logado"]:
    st.warning("Você precisa fazer login para acessar esta página.")
    st.stop()

page_header("Gerenciamento de Pets", "Cadastre os pacientes e vincule-os aos seus tutores.")

col1, col2 = st.columns([1, 2])

tutores = get_tutores()
tutores_options = {t["id"]: t["nome"] for t in tutores}

with col1:
    st.subheader("Cadastrar Novo Pet")
    if not tutores_options:
        st.warning("Cadastre um tutor primeiro para poder cadastrar um pet.")
    else:
        with st.form("form_pet"):
            nome = st.text_input("Nome do Pet")
            especie = st.selectbox("Espécie", ["Cachorro", "Gato", "Ave", "Roedor", "Outros"])
            raca = st.text_input("Raça")
            tutor_selecionado = st.selectbox("Tutor", options=list(tutores_options.keys()), format_func=lambda x: tutores_options[x])
            
            submit = st.form_submit_button("Salvar Pet", type="primary", width="stretch")
            if submit:
                erros = []
                if not nome:
                    erros.append("O nome do pet é obrigatório.")
                if not tutor_selecionado:
                    erros.append("Selecione um tutor válido.")

                if not erros:
                    create_pet({
                        "nome": nome,
                        "especie": especie,
                        "raca": raca,
                        "tutor_id": tutor_selecionado
                    })
                    st.success(f"Pet {nome} cadastrado com sucesso!")
                    st.rerun()
                else:
                    for erro in erros:
                        st.error(erro)

with col2:
    st.subheader("Pets Cadastrados")
    pets = get_pets()
    if pets:
        df = pd.DataFrame(pets)
        df["tutor_nome"] = df["tutor_id"].map(tutores_options)
        st.dataframe(df, width="stretch", hide_index=True)
    else:
        st.info("Nenhum pet cadastrado.")
