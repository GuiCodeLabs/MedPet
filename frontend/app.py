import streamlit as st
from services.api_client import login
from components.ui import load_css

# Configuração da Página
st.set_page_config(page_title="MedPet", page_icon="🐾", layout="wide")
load_css()

# Inicializar estado de sessão
if "logado" not in st.session_state:
    st.session_state["logado"] = False
if "token" not in st.session_state:
    st.session_state["token"] = None

def do_login():
    email = st.session_state.email_input
    senha = st.session_state.senha_input
    
    resp = login(email, senha)
    if resp:
        st.session_state["logado"] = True
        st.session_state["token"] = resp["token"]
        st.session_state["perfil"] = resp["perfil"]
        st.session_state["nome"] = resp.get("nome", "Usuário")
        st.rerun()
    else:
        st.error("E-mail ou senha inválidos. Por favor, tente novamente.")

if not st.session_state["logado"]:
    # Renderizar tela de Login centralizada simulando Tailwind (front.md)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<h1 class='login-title'>MedPet 🐾</h1>", unsafe_allow_html=True)
        st.markdown("<p class='login-subtitle'>Acesse sua conta para gerenciar sua clínica.</p>", unsafe_allow_html=True)
        
        with st.container():
            st.text_input("E-mail", key="email_input", placeholder="contato@exemplo.com.br")
            st.text_input("Senha", key="senha_input", type="password", placeholder="••••••••")
            st.button("Entrar", on_click=do_login, type="primary", width="stretch")
else:
    # Navegação do App (quando logado)
    pages = [
        st.Page("pages/1_dashboard.py", title="Dashboard", icon="📊", default=True),
        st.Page("pages/2_tutores.py", title="Tutores", icon="👥"),
        st.Page("pages/3_pets.py", title="Pets", icon="🐾"),
        st.Page("pages/4_consultas.py", title="Consultas", icon="🩺"),
        st.Page("pages/6_relatorios.py", title="Relatórios", icon="📁"),
    ]
    
    # Adicionar página de usuários apenas para admin
    if st.session_state.get("perfil") == "admin":
        pages.append(st.Page("pages/5_usuarios.py", title="Usuários", icon="🔐"))

    pg = st.navigation(pages)
    
    with st.sidebar:
        st.markdown(f"**Dr(a). {st.session_state.get('nome')}**")
        st.caption(f"Perfil: {st.session_state.get('perfil').capitalize()}")
        st.markdown("---")
        if st.button("Sair", width="stretch"):
            st.session_state["logado"] = False
            st.session_state["token"] = None
            st.rerun()
            
    pg.run()
