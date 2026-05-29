# 🧪 Estratégia de Testes — MedPet

Este documento descreve a organização e o procedimento para execução e escrita de testes automatizados no **MedPet**.

---

## 1. Organização dos Testes

O projeto utiliza o framework **Pytest** para validar de forma determinística tanto as regras isoladas de negócio quanto a integração dos endpoints REST. Os testes são organizados na pasta raiz `tests/`:

* **`tests/unit/`**: Testes unitários para validar a lógica de domínio interna e as regras nos Services sem requisições HTTP.
* **`tests/api/`**: Testes de integração das rotas HTTP, simulando chamadas à API com payload JSON e checando cabeçalhos e status codes.
* **`tests/conftest.py`**: Arquivo de configurações globais e fixtures compartilhadas pelo Pytest.

---

## 2. Banco de Dados Isolado para Testes

Para garantir que os testes rodem de forma isolada, limpa e rápida sem corromper ou alterar o banco de dados local (`clinica_veterinaria.db`), os testes utilizam um banco **SQLite em memória**:

> [!TIP]
> **Como funciona o Banco em Memória (`sqlite:///:memory:`)**
> 1. Antes de cada função de teste iniciar, o banco é criado do zero (`Base.metadata.create_all`).
> 2. As transações do teste ocorrem direto na memória RAM da máquina.
> 3. Após a finalização da função de teste, as tabelas são descartadas (`Base.metadata.drop_all`), garantindo que o próximo teste comece com um banco 100% limpo.

---

## 3. Como Executar os Testes Localmente

Siga o procedimento correspondente ao seu sistema operacional para rodar os testes:

### Passo 1: Ativação do Ambiente Virtual (`venv`)
* **No Windows (PowerShell)**:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
* **No Linux / macOS**:
  ```bash
  source .venv/bin/activate
  ```

### Passo 2: Definir PYTHONPATH e Executar o Pytest
O Pytest precisa conhecer o diretório `backend` para localizar o pacote `app`.

* **No Windows (PowerShell)**:
  ```powershell
  $env:PYTHONPATH="backend"
  pytest tests/
  ```
* **No Linux / macOS ou Git Bash**:
  ```bash
  PYTHONPATH=backend pytest tests/
  ```

---

## 4. Dicas Úteis de Execução do Pytest

* **Modo Verboso (Lista detalhada de testes)**:
  ```bash
  pytest tests/ -v
  ```
* **Exibir Saída de Console (`print` statements)**:
  ```bash
  pytest tests/ -s
  ```
* **Rodar apenas testes de um arquivo**:
  ```bash
  pytest tests/api/test_cliente.py
  ```

---

## 5. Escrevendo Novos Casos de Teste

> [!IMPORTANT]
> **Padrões de Nomenclatura**
> * **Arquivos de Teste**: Devem começar com o prefixo `test_` (ex: `test_pet.py`).
> * **Funções de Teste**: Devem começar com o prefixo `test_` (ex: `def test_cadastrar_pet_sucesso(client):`).
> * **Fixtures**: Use `db` para testes de serviços unitários e `client` para simular requisições HTTP na API.
