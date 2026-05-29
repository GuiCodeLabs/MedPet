import re

def is_valid_cpf(cpf: str) -> bool:
    """Verifica se o CPF possui 11 dígitos."""
    numeros = re.sub(r'[^0-9]', '', cpf)
    return len(numeros) == 11

def is_valid_email(email: str) -> bool:
    """Verifica formato básico de e-mail."""
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def is_valid_phone(phone: str) -> bool:
    """Verifica se o telefone possui 10 ou 11 dígitos (com DDD)."""
    numeros = re.sub(r'[^0-9]', '', phone)
    return 10 <= len(numeros) <= 11
