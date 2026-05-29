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
            motivo = st.text_area("Motivo da consulta / Sintomas")
            descricao = st.text_area("Observações adicionais", value="")
            submit = st.form_submit_button("Agendar", type="primary", use_container_width=True)
        
        if submit:
            erros = []
            if not pet_selecionado:
                erros.append("Selecione um pet válido.")
            if not motivo or not motivo.strip():
                erros.append("O motivo da consulta é obrigatório.")
                
            if not erros:
                try:
                    create_consulta({
                        "motivo": motivo,
                        "descricao": descricao if descricao.strip() else None,
                        "pet_id": pet_selecionado
                    })
                    st.success("Consulta agendada com sucesso!")
                    st.rerun()
                except Exception:
                    st.error("Não foi possível agendar a consulta. Verifique se a API está disponível e tente novamente.")
            else:
                for erro in erros:
                    st.error(erro)

with col2:
    st.subheader("Histórico e Próximas Consultas")
    try:
        consultas = get_consultas()
        if consultas:
            # Formatar dados para exibição
            dados_exibicao = []
            for c in consultas:
                dados_exibicao.append({
                    "ID": c.get("id"),
                    "Pet ID": c.get("pet_id"),
                    "Motivo": c.get("motivo"),
                    "Observações": c.get("descricao", "-"),
                    "Data": c.get("data", "-")
                })
            df = pd.DataFrame(dados_exibicao)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Nenhuma consulta agendada.")
    except Exception as e:
        st.error(f"Erro ao carregar consultas: {str(e)}")
        st.info("Verifique se a API está disponível.")
