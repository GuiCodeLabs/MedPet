import streamlit as st
import pandas as pd
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.ui import page_header, load_css
from utils.export import generate_excel_download, generate_csv_download
from services.api_client import get_consultas

st.set_page_config(page_title="Relatórios - MedPet", page_icon="📁", layout="wide")
load_css()

if "logado" not in st.session_state or not st.session_state["logado"]:
    st.warning("Você precisa fazer login para acessar esta página.")
    st.stop()

page_header("Relatórios", "Exporte os dados da clínica para análise.")

# Buscar dados do backend
consultas = get_consultas()
df = pd.DataFrame(consultas)

st.subheader("Filtros")
col1, col2 = st.columns(2)
with col1:
    data_inicio = st.date_input("Data Início")
with col2:
    data_fim = st.date_input("Data Fim")

st.markdown("---")

# Aplicar filtro de datas se o DataFrame tiver dados e uma coluna de data
if not df.empty and "data" in df.columns:
    try:
        df["data_parsed"] = pd.to_datetime(df["data"], errors="coerce").dt.date
        df_filtrado = df[
            (df["data_parsed"] >= data_inicio) & (df["data_parsed"] <= data_fim)
        ].drop(columns=["data_parsed"])
    except Exception:
        df_filtrado = df
elif not df.empty and "criado_em" in df.columns:
    try:
        df["data_parsed"] = pd.to_datetime(df["criado_em"], errors="coerce").dt.date
        df_filtrado = df[
            (df["data_parsed"] >= data_inicio) & (df["data_parsed"] <= data_fim)
        ].drop(columns=["data_parsed"])
    except Exception:
        df_filtrado = df
else:
    df_filtrado = df

st.subheader("Visualização dos Dados")
if df_filtrado.empty:
    st.info("Nenhuma consulta encontrada no período selecionado.")
else:
    st.dataframe(df_filtrado, width="stretch", hide_index=True)

st.markdown("### Exportar")
c1, c2, c3 = st.columns(3)

excel_data = generate_excel_download(df_filtrado)
csv_data = generate_csv_download(df_filtrado)

with c1:
    st.download_button(
        label="📄 Baixar Excel",
        data=excel_data,
        file_name="relatorio_consultas.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        width="stretch"
    )

with c2:
    st.download_button(
        label="📄 Baixar CSV",
        data=csv_data,
        file_name="relatorio_consultas.csv",
        mime="text/csv",
        width="stretch"
    )
