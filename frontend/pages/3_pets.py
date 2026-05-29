import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.ui import page_header, load_css
from services.api_client import get_pets, get_tutores, create_pet

def calcular_idade_humana(especie, idade):
    if idade is None or idade < 0:
        return None
    if especie == "Cachorro":
        if idade == 0: return 0
        if idade == 1: return 15
        if idade == 2: return 24
        return 24 + (idade - 2) * 5
    elif especie == "Gato":
        if idade == 0: return 0
        if idade == 1: return 15
        if idade == 2: return 24
        return 24 + (idade - 2) * 4
    return None

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
        with st.container(border=True):
            nome = st.text_input("Nome do Pet", max_chars=50)
            especie_selecionada = st.selectbox("Espécie", ["Cachorro", "Gato", "Ave", "Roedor", "Outros"])
            if especie_selecionada == "Outros":
                especie = st.text_input("Qual espécie?", max_chars=30)
            else:
                especie = especie_selecionada
            raca = st.text_input("Raça", max_chars=50)
            col_idade, col_peso = st.columns(2)
            with col_idade:
                idade = st.number_input("Idade (anos)", min_value=0, step=1, value=None)
                idade_humana = calcular_idade_humana(especie, idade)
                if idade_humana is not None:
                    st.caption(f"🐾 Idade humana aprox: **{idade_humana} anos**")
            with col_peso:
                peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1, value=None, format="%.1f")
            tutor_selecionado = st.selectbox("Tutor", options=list(tutores_options.keys()), format_func=lambda x: tutores_options[x])
            
            submit = st.button("Salvar Pet", type="primary", use_container_width=True)
            if submit:
                erros = []
                if not nome:
                    erros.append("O nome do pet é obrigatório.")
                if especie_selecionada == "Outros" and not especie:
                    erros.append("Por favor, especifique a espécie do pet.")
                if not tutor_selecionado:
                    erros.append("Selecione um tutor válido.")

                if not erros:
                    create_pet({
                        "nome": nome,
                        "especie": especie,
                        "raca": raca,
                        "idade": idade,
                        "peso": peso,
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
