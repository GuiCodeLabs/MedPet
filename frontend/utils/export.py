import pandas as pd
import io

def generate_excel_download(df, filename="relatorio.xlsx"):
    """Gera um buffer de bytes contendo um arquivo Excel a partir de um DataFrame"""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Dados')
    return output.getvalue()

def generate_csv_download(df):
    """Gera um buffer de string contendo um arquivo CSV a partir de um DataFrame"""
    return df.to_csv(index=False).encode('utf-8')
