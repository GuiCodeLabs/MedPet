"""
Módulo para geração de comprovantes de consulta em PDF.
Usa fpdf2 para criar um documento profissional com os dados do atendimento.
"""
from fpdf import FPDF
from datetime import datetime
import io


class ComprovantePDF(FPDF):
    """PDF personalizado com cabeçalho e rodapé da clínica."""

    def __init__(self, nome_clinica="MedPet - Clínica Veterinária"):
        super().__init__()
        self.nome_clinica = nome_clinica

    def header(self):
        # ── Faixa superior com cor da marca ──
        self.set_fill_color(37, 99, 235)  # Azul profissional
        self.rect(0, 0, 210, 38, "F")

        # Nome da clínica
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(255, 255, 255)
        self.set_y(8)
        self.cell(0, 10, self.nome_clinica, align="C", new_x="LMARGIN", new_y="NEXT")

        # Subtítulo
        self.set_font("Helvetica", "", 10)
        self.set_text_color(200, 220, 255)
        self.cell(0, 6, "Comprovante de Atendimento Veterinário", align="C", new_x="LMARGIN", new_y="NEXT")

        self.ln(16)

    def footer(self):
        self.set_y(-25)

        # Linha divisória
        self.set_draw_color(200, 200, 200)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(4)

        # Texto do rodapé
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(130, 130, 130)
        self.cell(0, 4, "Este comprovante foi gerado automaticamente pelo sistema MedPet.", align="C", new_x="LMARGIN", new_y="NEXT")

        emitido = datetime.now().strftime("%d/%m/%Y às %H:%M")
        self.cell(0, 4, f"Emitido em: {emitido}", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 4, f"Página {self.page_no()}/{{nb}}", align="C")

    def _section_title(self, titulo):
        """Desenha um título de seção com fundo colorido."""
        self.set_font("Helvetica", "B", 11)
        self.set_fill_color(240, 245, 255)
        self.set_text_color(37, 99, 235)
        self.cell(0, 9, f"  {titulo}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def _info_row(self, label, valor):
        """Desenha uma linha de informação com label em negrito."""
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(60, 60, 60)
        self.cell(55, 7, f"{label}:", new_x="RIGHT")

        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.cell(0, 7, str(valor) if valor else "-", new_x="LMARGIN", new_y="NEXT")

    def _divider(self):
        """Linha divisória fina e sutil."""
        self.ln(2)
        self.set_draw_color(220, 220, 220)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(5)


def gerar_comprovante(consulta, pet_info=None, tutor_info=None):
    """
    Gera o PDF do comprovante de consulta e retorna os bytes.

    Args:
        consulta: dict com dados da consulta (motivo, data, status, etc.)
        pet_info: dict com dados do pet (nome, especie, raca, idade, peso)
        tutor_info: dict com dados do tutor (nome, telefone, email)

    Returns:
        bytes do PDF pronto para download
    """
    pdf = ComprovantePDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=30)

    # ══════════════════════════════════════════
    # NÚMERO DO ATENDIMENTO
    # ══════════════════════════════════════════
    consulta_id = consulta.get("id", "---")
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 10, f"Atendimento #{consulta_id}", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    # ══════════════════════════════════════════
    # DADOS DO PET
    # ══════════════════════════════════════════
    pdf._section_title("Dados do Paciente (Pet)")

    nome_pet = consulta.get("Pet", "")
    if pet_info:
        nome_pet = pet_info.get("nome", nome_pet)
        pdf._info_row("Nome", nome_pet)
        pdf._info_row("Espécie", pet_info.get("especie", "-"))
        pdf._info_row("Raça", pet_info.get("raca", "-"))
        if pet_info.get("idade") is not None:
            pdf._info_row("Idade", f"{pet_info['idade']} ano(s)")
        if pet_info.get("peso") is not None:
            pdf._info_row("Peso", f"{pet_info['peso']} kg")
    else:
        pdf._info_row("Nome", nome_pet)

    pdf._divider()

    # ══════════════════════════════════════════
    # DADOS DO TUTOR
    # ══════════════════════════════════════════
    if tutor_info:
        pdf._section_title("Dados do Tutor")
        pdf._info_row("Nome", tutor_info.get("nome", "-"))
        pdf._info_row("Telefone", tutor_info.get("telefone", "-"))
        pdf._info_row("E-mail", tutor_info.get("email", "-"))
        pdf._divider()

    # ══════════════════════════════════════════
    # DADOS DA CONSULTA
    # ══════════════════════════════════════════
    pdf._section_title("Detalhes do Atendimento")

    pdf._info_row("Motivo", consulta.get("Motivo", consulta.get("motivo", "-")))
    pdf._info_row("Data", consulta.get("Data", "-"))
    pdf._info_row("Horário", consulta.get("Horário", consulta.get("Horario", "-")))

    status = consulta.get("Status", consulta.get("status", "Agendada"))
    status_labels = {
        "Agendada": "Agendada",
        "Em andamento": "Em Andamento",
        "Concluída": "Concluída",
        "Cancelada": "Cancelada"
    }
    pdf._info_row("Status", status_labels.get(status, status))

    obs = consulta.get("Observações", consulta.get("descricao", ""))
    if obs and obs != "-":
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(55, 7, "Observações:", new_x="LMARGIN", new_y="NEXT")

        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(30, 30, 30)
        pdf.multi_cell(0, 6, str(obs))

    pdf._divider()

    # ══════════════════════════════════════════
    # ÁREA DE ASSINATURA
    # ══════════════════════════════════════════
    pdf.ln(15)

    # Assinatura do Veterinário
    x_center = 105
    line_width = 70

    pdf.set_draw_color(100, 100, 100)
    pdf.line(x_center - line_width / 2, pdf.get_y(), x_center + line_width / 2, pdf.get_y())
    pdf.ln(3)

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 5, "Assinatura do(a) Veterinário(a)", align="C", new_x="LMARGIN", new_y="NEXT")

    # ── Gerar bytes ──
    return pdf.output()
