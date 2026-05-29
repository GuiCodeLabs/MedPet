import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.ui import metric_card, page_header, load_css
from services.api_client import get_consultas, get_pets, get_tutores

st.set_page_config(page_title="Dashboard - MedPet", page_icon="🐾", layout="wide")
load_css()

if "logado" not in st.session_state or not st.session_state["logado"]:
    st.warning("Você precisa fazer login para acessar esta página.")
    st.stop()

page_header(f"Bom dia, {st.session_state.get('nome', 'Usuário')}.", "Aqui está o resumo da sua clínica hoje.")

col1, col2, col3, _ = st.columns([2, 2, 2, 4])
with col1:
    if st.button("➕ Cadastrar Tutor", width="stretch"):
        st.switch_page("pages/2_tutores.py")
with col2:
    if st.button("🐾 Cadastrar Pet", width="stretch"):
        st.switch_page("pages/3_pets.py")
with col3:
    if st.button("📅 Nova Consulta", width="stretch", type="primary"):
        st.switch_page("pages/4_consultas.py")

st.markdown("---")

pets_cadastrados = get_pets()
tutores_cadastrados = get_tutores()
consultas_todas = get_consultas()
consultas_pendentes = [c for c in consultas_todas if c["status"] != "Concluída"]

c1, c2, c3, c4 = st.columns(4)
with c1:
    metric_card("Total de Pets", str(len(pets_cadastrados)), "🐾")
with c2:
    metric_card("Total de Tutores", str(len(tutores_cadastrados)), "👥")
with c3:
    metric_card("Consultas do Dia", str(len(consultas_todas)), "📅")
with c4:
    metric_card("Consultas Pendentes", str(len(consultas_pendentes)), "⏳")

st.markdown("<br>", unsafe_allow_html=True)

col_tabela, col_grafico = st.columns([2, 1])

with col_tabela:
    st.subheader("Consultas Recentes")
    df_consultas = pd.DataFrame(consultas_todas)
    st.dataframe(df_consultas, width="stretch", hide_index=True)

with col_grafico:
    st.subheader("Consultas por Status")
    status_concluidas = len([c for c in consultas_todas if c["status"] == "Concluída"])
    status_andamento = len([c for c in consultas_todas if c["status"] == "Em andamento"])
    status_agendada = len([c for c in consultas_todas if c["status"] == "Agendada"])
    
    df_status = pd.DataFrame({
        "Status": ["Concluídas", "Em andamento", "Agendadas"],
        "Quantidade": [status_concluidas, status_andamento, status_agendada]
    })
    st.bar_chart(df_status.set_index("Status"))
