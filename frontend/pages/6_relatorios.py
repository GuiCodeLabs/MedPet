import streamlit as st
import pandas as pd
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.ui import page_header, load_css
from utils.export import generate_excel_download, generate_csv_download, generate_pdf_download
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

df_filtrado = df.copy()

# Tratamento e mapeamento do DataFrame para exibição e exportação
if not df_filtrado.empty:
    # Garantir que a data é parseável
    if "data" in df_filtrado.columns:
        df_filtrado["data_parsed"] = pd.to_datetime(df_filtrado["data"], errors="coerce")
        df_filtrado["Data"] = df_filtrado["data_parsed"].dt.strftime("%d/%m/%Y")
        df_filtrado["Horário"] = df_filtrado["data_parsed"].dt.strftime("%H:%M")
        
        # Filtro de datas
        df_filtrado = df_filtrado[
            (df_filtrado["data_parsed"].dt.date >= data_inicio) & 
            (df_filtrado["data_parsed"].dt.date <= data_fim)
        ]
        
    # Mapear e selecionar colunas úteis
    colunas_map = {
        "id": "ID",
        "pet": "Paciente (Pet)",
        "motivo": "Motivo",
        "status": "Status",
        "descricao": "Observações"
    }
    
    # Renomear as que existem
    df_filtrado.rename(columns=colunas_map, inplace=True)
    
    # Preencher observações vazias com "-"
    if "Observações" in df_filtrado.columns:
        df_filtrado["Observações"] = df_filtrado["Observações"].fillna("-")
    
    # Manter só as colunas que nos interessam e na ordem certa
    colunas_finais = ["ID", "Data", "Horário", "Paciente (Pet)", "Motivo", "Status", "Observações"]
    colunas_presentes = [c for c in colunas_finais if c in df_filtrado.columns]
    
    df_filtrado = df_filtrado[colunas_presentes]


st.subheader("Visualização dos Dados")
if df_filtrado.empty:
    st.info("Nenhuma consulta encontrada no período selecionado.")
else:
    st.dataframe(df_filtrado, width="stretch", hide_index=True)

st.markdown("### Exportar")
if not df_filtrado.empty:
    c1, c2, c3 = st.columns(3)

    excel_data = generate_excel_download(df_filtrado)
    csv_data = generate_csv_download(df_filtrado)
    pdf_data = generate_pdf_download(df_filtrado)

    with c1:
        st.download_button(
            label="📊 Baixar Excel",
            data=excel_data,
            file_name="relatorio_consultas.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

    with c2:
        st.download_button(
            label="📄 Baixar PDF",
            data=pdf_data,
            file_name="relatorio_consultas.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    with c3:
        st.download_button(
            label="📝 Baixar CSV",
            data=csv_data,
            file_name="relatorio_consultas.csv",
            mime="text/csv",
            use_container_width=True
        )
