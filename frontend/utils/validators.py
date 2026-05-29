import re

def is_valid_cpf(cpf: str) -> bool:
    """Verifica se o CPF possui 11 dígitos e se é um CPF válido pelas regras matemáticas."""
    numeros = re.sub(r'[^0-9]', '', cpf)
    if len(numeros) != 11 or len(set(numeros)) == 1:
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = sum(int(numeros[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 >= 10:
        digito1 = 0
        
    # Cálculo do segundo dígito verificador
    soma = sum(int(numeros[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    if digito2 >= 10:
        digito2 = 0
        
    return int(numeros[9]) == digito1 and int(numeros[10]) == digito2

def is_valid_email(email: str) -> bool:
    """Verifica formato básico de e-mail."""
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def is_valid_phone(phone: str) -> bool:
    """Verifica se o telefone possui 10 ou 11 dígitos (com DDD)."""
    numeros = re.sub(r'[^0-9]', '', phone)
    return 10 <= len(numeros) <= 11
