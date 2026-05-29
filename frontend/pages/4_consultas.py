import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.ui import page_header, load_css
from services.api_client import get_consultas, get_pets, create_consulta

st.set_page_config(page_title="Consultas - MedPet", page_icon="🩺", layout="wide")
load_css()

if "logado" not in st.session_state or not st.session_state["logado"]:
    st.warning("Você precisa fazer login para acessar esta página.")
    st.stop()

page_header("Agenda de Consultas", "Agende e gerencie os atendimentos da clínica.")

col1, col2 = st.columns([1, 2])

pets = get_pets()
pets_options = {p["id"]: p["nome"] for p in pets}

with col1:
    st.subheader("Agendar Consulta")
    if not pets_options:
        st.warning("Cadastre um pet primeiro para poder agendar uma consulta.")
    else:
        with st.form("form_consulta"):
            pet_selecionado = st.selectbox("Pet Paciente", options=list(pets_options.keys()), format_func=lambda x: pets_options[x])
            data_hora = st.date_input("Data da Consulta")
            hora = st.time_input("Horário")
            motivo = st.text_area("Motivo da consulta / Sintomas")
            
            submit = st.form_submit_button("Agendar", type="primary", width="stretch")
            if submit:
                erros = []
                if not pet_selecionado:
                    erros.append("Selecione um pet válido.")
                if not motivo:
                    erros.append("O motivo da consulta é obrigatório.")
                    
                if not erros:
                    create_consulta({
                        "data": f"{data_hora} {hora}",
                        "pet_id": pet_selecionado,
                        "pet": pets_options[pet_selecionado],
                        "status": "Agendada",
                        "motivo": motivo
                    })
                    st.success("Consulta agendada com sucesso!")
                    st.rerun()
                else:
                    for erro in erros:
                        st.error(erro)

with col2:
    st.subheader("Histórico e Próximas Consultas")
    consultas = get_consultas()
    if consultas:
        df = pd.DataFrame(consultas)
        st.dataframe(df, width="stretch", hide_index=True)
    else:
        st.info("Nenhuma consulta agendada.")
