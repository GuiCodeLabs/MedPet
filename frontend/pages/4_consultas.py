import streamlit as st
import pandas as pd
from datetime import datetime, date, time, timedelta
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.ui import page_header, load_css
from services.api_client import get_consultas, get_pets, get_tutores, create_consulta, update_consulta
from services.pdf_comprovante import gerar_comprovante

st.set_page_config(page_title="Consultas - MedPet", page_icon="🩺", layout="wide")
load_css()

if "logado" not in st.session_state or not st.session_state["logado"]:
    st.warning("Você precisa fazer login para acessar esta página.")
    st.stop()

page_header("Agenda de Consultas", "Agende e gerencie os atendimentos da clínica.")

# ─── Constantes ───
MOTIVOS_PADRAO = [
    "Consulta de Rotina",
    "Vacinação",
    "Retorno",
    "Exame",
    "Cirurgia",
    "Emergência",
    "Outros"
]

STATUS_CORES = {
    "Agendada": "🔵",
    "Em andamento": "🟡",
    "Concluída": "🟢",
    "Cancelada": "🔴"
}

STATUS_OPTIONS = list(STATUS_CORES.keys())

# ─── Carregar dados auxiliares (pets e tutores) ───
pets = get_pets()
pets_options = {p["id"]: p["nome"] for p in pets}
pets_map = {p["id"]: p for p in pets}  # mapa completo para o PDF

tutores = get_tutores()
tutores_map = {t["id"]: t for t in tutores}  # mapa id -> tutor

# ─── Layout principal ───
col1, col2 = st.columns([1, 2])

# ══════════════════════════════════════════════════
# COLUNA 1 — Formulário de Agendamento
# ══════════════════════════════════════════════════
with col1:
    st.subheader("📋 Agendar Consulta")

    if not pets_options:
        st.warning("Cadastre um pet primeiro para poder agendar uma consulta.")
    else:
        with st.form("form_consulta"):
            pet_selecionado = st.selectbox(
                "Pet Paciente",
                options=list(pets_options.keys()),
                format_func=lambda x: pets_options[x]
            )

            # ── Data e Hora ──
            col_data, col_hora = st.columns(2)
            with col_data:
                data_consulta = st.date_input(
                    "Data",
                    value=date.today(),
                    min_value=date.today(),
                    format="DD/MM/YYYY"
                )
            with col_hora:
                hora_consulta = st.time_input(
                    "Horário",
                    value=time(9, 0),
                    step=timedelta(minutes=30)
                )

            # ── Motivo padronizado ──
            motivo_selecionado = st.selectbox("Motivo", MOTIVOS_PADRAO)

            motivo_personalizado = ""
            if motivo_selecionado == "Outros":
                motivo_personalizado = st.text_input(
                    "Especifique o motivo",
                    max_chars=100,
                    placeholder="Descreva brevemente..."
                )

            # ── Observações ──
            descricao = st.text_area(
                "Observações adicionais",
                value="",
                max_chars=500,
                placeholder="Ex: animal em jejum, trazer exames anteriores..."
            )

            submit = st.form_submit_button(
                "🩺 Agendar Consulta",
                type="primary",
                use_container_width=True
            )

        if submit:
            erros = []
            if not pet_selecionado:
                erros.append("Selecione um pet válido.")

            # Definir o motivo final
            if motivo_selecionado == "Outros":
                if not motivo_personalizado or not motivo_personalizado.strip():
                    erros.append("Especifique o motivo da consulta.")
                else:
                    motivo_final = f"Outros: {motivo_personalizado.strip()}"
            else:
                motivo_final = motivo_selecionado

            if not erros:
                try:
                    # Combinar data e hora em datetime ISO 8601
                    data_hora = datetime.combine(data_consulta, hora_consulta)

                    create_consulta({
                        "motivo": motivo_final,
                        "descricao": descricao.strip() if descricao.strip() else None,
                        "pet_id": pet_selecionado,
                        "data": data_hora.isoformat(),
                        "status": "Agendada"
                    })
                    st.success("✅ Consulta agendada com sucesso!")
                    st.rerun()
                except Exception:
                    st.error("Não foi possível agendar a consulta. Verifique se a API está disponível.")
            else:
                for erro in erros:
                    st.error(erro)


# ══════════════════════════════════════════════════
# COLUNA 2 — Visualização com Abas
# ══════════════════════════════════════════════════
with col2:
    try:
        consultas = get_consultas()

        if not consultas:
            st.info("📭 Nenhuma consulta agendada ainda.")
        else:
            # Separar consultas em futuras e passadas
            agora = datetime.now()
            proximas = []
            historico = []

            for c in consultas:
                data_str = c.get("data", "")
                status = c.get("status", "Agendada")
                try:
                    data_parsed = datetime.fromisoformat(data_str.replace("Z", "+00:00"))
                    # Remove tzinfo para comparação simples
                    data_naive = data_parsed.replace(tzinfo=None)
                except (ValueError, AttributeError):
                    data_naive = agora  # fallback

                registro = {
                    "id": c.get("id"),
                    "pet_id": c.get("pet_id"),
                    "Pet": c.get("pet", "Desconhecido"),
                    "Motivo": c.get("motivo", "-"),
                    "Observações": c.get("descricao") or "-",
                    "Data": data_naive.strftime("%d/%m/%Y"),
                    "Horário": data_naive.strftime("%H:%M"),
                    "Status": status,
                    "_status_icon": STATUS_CORES.get(status, "⚪"),
                    "_datetime": data_naive
                }

                # Futuras: data >= hoje E status não é Concluída/Cancelada
                if data_naive >= agora and status not in ("Concluída", "Cancelada"):
                    proximas.append(registro)
                else:
                    historico.append(registro)

            # Ordenar
            proximas.sort(key=lambda x: x["_datetime"])
            historico.sort(key=lambda x: x["_datetime"], reverse=True)

            tab_proximas, tab_historico = st.tabs(["📅 Próximas Consultas", "📜 Histórico"])

            # ── Função para renderizar cards com status e comprovante ──
            def renderizar_tabela(registros, tab_key):
                if not registros:
                    st.info("Nenhuma consulta nesta categoria.")
                    return

                for i, reg in enumerate(registros):
                    icon = reg["_status_icon"]
                    with st.container(border=True):
                        c1, c2, c3 = st.columns([3, 2, 2])
                        with c1:
                            st.markdown(f"**{icon} {reg['Pet']}** — {reg['Motivo']}")
                            if reg["Observações"] != "-":
                                st.caption(f"📝 {reg['Observações']}")
                        with c2:
                            st.markdown(f"📅 **{reg['Data']}** às **{reg['Horário']}**")
                        with c3:
                            status_atual = reg["Status"]
                            novo_status = st.selectbox(
                                "Status",
                                STATUS_OPTIONS,
                                index=STATUS_OPTIONS.index(status_atual) if status_atual in STATUS_OPTIONS else 0,
                                key=f"status_{tab_key}_{reg['id']}_{i}",
                                label_visibility="collapsed"
                            )
                            if novo_status != status_atual:
                                update_consulta(reg["id"], {"status": novo_status})
                                st.rerun()

                        # ── Botão de Comprovante PDF ──
                        # Buscar dados completos do pet e tutor para o PDF
                        pet_id = reg.get("pet_id")
                        pet_data = pets_map.get(pet_id, {})
                        tutor_id = pet_data.get("tutor_id") or pet_data.get("cliente_id")
                        tutor_data = tutores_map.get(tutor_id, {}) if tutor_id else {}

                        try:
                            pdf_bytes = gerar_comprovante(
                                consulta=reg,
                                pet_info=pet_data if pet_data else None,
                                tutor_info=tutor_data if tutor_data else None
                            )

                            nome_arquivo = f"comprovante_consulta_{reg['id']}_{reg['Data'].replace('/', '-')}.pdf"

                            st.download_button(
                                label="📄 Baixar Comprovante",
                                data=pdf_bytes,
                                file_name=nome_arquivo,
                                mime="application/pdf",
                                key=f"pdf_{tab_key}_{reg['id']}_{i}",
                                use_container_width=True
                            )
                        except Exception as e:
                            st.error(f"Erro ao gerar PDF: {e}")

            with tab_proximas:
                st.caption(f"**{len(proximas)}** consulta(s) agendada(s)")
                renderizar_tabela(proximas, "prox")

            with tab_historico:
                st.caption(f"**{len(historico)}** consulta(s) no histórico")
                renderizar_tabela(historico, "hist")

    except Exception as e:
        st.error(f"Erro ao carregar consultas: {str(e)}")
        st.info("Verifique se a API está disponível.")
