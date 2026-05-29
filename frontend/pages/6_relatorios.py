import streamlit as st
import pandas as pd
import sys
import os

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

# Mock data
df = pd.DataFrame(get_consultas())

st.subheader("Filtros")
col1, col2 = st.columns(2)
with col1:
    data_inicio = st.date_input("Data Início")
with col2:
    data_fim = st.date_input("Data Fim")

st.markdown("---")

st.subheader("Visualização dos Dados")
st.dataframe(df, width="stretch")

st.markdown("### Exportar")
c1, c2, c3 = st.columns(3)

excel_data = generate_excel_download(df)
csv_data = generate_csv_download(df)

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
