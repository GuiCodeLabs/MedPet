import streamlit as st
import os

def load_css():
    """Carrega o arquivo CSS estático e injeta no Streamlit."""
    css_file = os.path.join(os.path.dirname(__file__), '..', 'assets', 'style.css')
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def metric_card(title, value, icon, color="blue"):
    """Renderiza um card de métrica customizado."""
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-card-content">
                <p class="metric-title">{title}</p>
                <p class="metric-value">{value}</p>
            </div>
            <div class="metric-card-icon">
                <span>{icon}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def page_header(title, description):
    """Renderiza o cabeçalho padronizado da página"""
    st.markdown(f"## {title}")
    st.markdown(f"<p class='page-header-desc'>{description}</p>", unsafe_allow_html=True)
