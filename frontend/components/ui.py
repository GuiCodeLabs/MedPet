import streamlit as st

def metric_card(title, value, icon, color="blue"):
    """
    Renderiza um card de mÃ©trica customizado simulando o layout do Tailwind.
    Como Streamlit nÃ£o permite injetar Tailwind puro facilmente sem iframes,
    usamos st.metric encapsulado ou HTML nativo via st.markdown
    """
    
    st.markdown(
        f"""
        <div style="background-color: white; padding: 20px; border-radius: 10px; border: 1px solid #e0e3e5; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
            <div>
                <p style="color: #727783; font-size: 12px; margin: 0 0 4px 0;">{title}</p>
                <p style="color: #191c1e; font-size: 24px; font-weight: 600; margin: 0;">{value}</p>
            </div>
            <div style="background-color: #f2f4f6; padding: 10px; border-radius: 8px;">
                <span style="font-size: 20px;">{icon}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def page_header(title, description):
    """Renderiza o cabeÃ§alho padronizado da pÃ¡gina"""
    st.markdown(f"## {title}")
    st.markdown(f"<p style='color: #727783; margin-top: -10px; margin-bottom: 20px;'>{description}</p>", unsafe_allow_html=True)
