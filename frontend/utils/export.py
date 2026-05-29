import pandas as pd
import io
from fpdf import FPDF
from datetime import datetime

def generate_excel_download(df):
    """Gera um arquivo Excel com colunas ajustadas e estilo"""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Relatorio')
        worksheet = writer.sheets['Relatorio']
        
        # Ajustar a largura das colunas
        for idx, col in enumerate(df.columns, 1):
            max_length = max(df[col].astype(str).map(len).max(), len(str(col))) + 2
            col_letter = chr(64 + idx) if idx <= 26 else chr(64 + idx // 26) + chr(64 + idx % 26)
            worksheet.column_dimensions[col_letter].width = max_length
            
            # Estilizar cabeçalho (negrito)
            cell = worksheet.cell(row=1, column=idx)
            cell.font = cell.font.copy(bold=True)
            
    return output.getvalue()

def generate_csv_download(df):
    """Gera CSV com separador ponto e vírgula e BOM (UTF-8) para o Excel abrir direto com acentos"""
    csv_str = df.to_csv(index=False, sep=";")
    return "\ufeff".encode('utf8') + csv_str.encode('utf-8')

class RelatorioPDF(FPDF):
    def header(self):
        self.set_fill_color(37, 99, 235)  # Azul
        self.rect(0, 0, 297, 25, "F")  # Landscape width
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(255, 255, 255)
        self.set_y(8)
        self.cell(0, 10, "Relatório de Atendimentos - MedPet", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)
        
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", align="C")

def generate_pdf_download(df):
    """Gera um PDF tabular com os dados do DataFrame"""
    pdf = RelatorioPDF(orientation="L")  # Paisagem
    pdf.alias_nb_pages()
    pdf.add_page()
    
    if df.empty:
        pdf.set_font("Helvetica", "", 12)
        pdf.cell(0, 10, "Nenhum dado encontrado para o relatorio.", align="C")
        return bytes(pdf.output())
    
    # Definir larguras das colunas baseado nas colunas presentes (ajuste específico para consultas)
    # Total disponível = 277mm
    # 'ID' (15), 'Data' (25), 'Horário' (20), 'Paciente (Pet)' (45), 'Motivo' (45), 'Status' (30), 'Observações' (97)
    colunas_conhecidas = {
        "ID": 12,
        "Data": 25,
        "Horário": 20,
        "Paciente (Pet)": 40,
        "Motivo": 45,
        "Status": 30,
        "Observações": 105
    }
    
    larguras = [colunas_conhecidas.get(col, 277 / len(df.columns)) for col in df.columns]
    
    # Cabeçalho
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_fill_color(240, 245, 255)
    pdf.set_text_color(37, 99, 235)
    
    for i, col in enumerate(df.columns):
        pdf.cell(larguras[i], 8, str(col).upper(), border=1, fill=True, align="C")
    pdf.ln()
    
    # Linhas
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(0, 0, 0)
    
    for _, row in df.iterrows():
        # Verificar altura máxima da linha baseada no texto mais longo (observações)
        # Vamos simplificar cortando o texto muito longo para caber em uma linha, ou usar altura padrão
        for i, item in enumerate(row):
            texto = str(item)
            # Limitar tamanho do texto para não quebrar a célula (aprox. 55 caracteres para a observação)
            limite_chars = int(larguras[i] * 0.55) 
            if len(texto) > limite_chars:
                texto = texto[:limite_chars-3] + "..."
            
            # Ajustar alinhamentos (ID, Data, Horário centralizados)
            align = "C" if df.columns[i] in ["ID", "Data", "Horário", "Status"] else "L"
            pdf.cell(larguras[i], 7, texto, border=1, align=align)
        pdf.ln()
        
    return bytes(pdf.output())
