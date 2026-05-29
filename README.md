# 🐾 MedPet — Sistema Web de Gestão para Clínica Veterinária

Projeto desenvolvido para a disciplina **Análise e Projeto de Sistemas (APS)**, com o objetivo de construir um sistema web simples, funcional e bem estruturado para auxiliar na gestão básica de uma clínica veterinária.

O sistema será desenvolvido com **FastAPI** no backend e **Streamlit** no frontend, seguindo a proposta do trabalho de criar uma aplicação web completa, com API, interface, banco de dados, documentação e organização baseada em boas práticas de Engenharia de Software.

---

## 📌 Sobre o Projeto

O **MedPet** tem como finalidade centralizar informações importantes de uma clínica veterinária, reduzindo controles manuais e facilitando o cadastro, consulta e organização de dados de clientes, pets e atendimentos.

Nesta primeira versão, o foco será entregar um sistema básico, coerente com o escopo acadêmico, contendo as funcionalidades essenciais para apresentação e validação do projeto.

---

## 🎯 Objetivo

Desenvolver uma aplicação web para gestão veterinária que permita:

- Cadastrar e consultar clientes;
- Cadastrar pets vinculados aos seus tutores;
- Registrar atendimentos veterinários;
- Organizar informações básicas da clínica;
- Demonstrar integração entre frontend, backend e banco de dados;
- Aplicar conceitos de Engenharia de Software, UML e padrões de projeto.

---

## 👥 Público-Alvo

O sistema é destinado a pequenas clínicas veterinárias, atendentes, veterinários e administradores que precisam organizar dados de clientes, animais e atendimentos de forma simples e centralizada.

---

## 👤 Perfis de Usuário

### Administrador
Responsável por gerenciar o sistema, visualizar dados gerais e manter os cadastros principais.

### Atendente
Responsável por cadastrar clientes, pets e consultar informações básicas.

### Veterinário
Responsável por registrar atendimentos, histórico clínico e observações sobre os pets.

---

## ✅ Funcionalidades do Sistema

### Clientes
- Cadastro de clientes/tutores;
- Listagem de clientes cadastrados;
- Atualização de dados cadastrais;
- Remoção de clientes, quando necessário.

### Pets
- Cadastro de pets;
- Associação de pets aos seus respectivos tutores;
- Consulta de informações como nome, espécie, raça, idade e observações;
- Atualização e exclusão de registros.

### Atendimentos
- Registro de atendimentos veterinários;
- Histórico de atendimentos por pet;
- Descrição do motivo da consulta;
- Observações clínicas básicas;
- Data do atendimento.

### Usuários e Autenticação
- Cadastro de usuários do sistema;
- Login com autenticação;
- Controle básico de acesso por perfil.

### Relatórios Simples
- Consulta de clientes cadastrados;
- Consulta de pets por tutor;
- Consulta de atendimentos registrados.

---

## 🧱 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

<br>

- **Python** — linguagem principal do projeto;
- **FastAPI** — criação da API REST;
- **Streamlit** — construção da interface web;
- **SQLAlchemy** — ORM para comunicação com o banco de dados;
- **SQLite** — banco de dados utilizado na versão inicial;
- **Pydantic** — validação dos dados da API;
- **Pytest** — testes automatizados;
- **JWT** — autenticação e segurança;
- **Git/GitHub** — versionamento e entrega do projeto.

---

## 🏗️ Arquitetura do Sistema

O projeto será dividido em três camadas principais:

1. **Frontend**  
   Interface web desenvolvida em Streamlit, responsável por exibir telas, formulários e tabelas para o usuário.

2. **Backend**  
   API REST desenvolvida em FastAPI, responsável pelas regras de negócio, autenticação e endpoints do sistema.

3. **Banco de Dados**  
   Camada de persistência responsável por armazenar usuários, clientes, pets e atendimentos.

A comunicação entre frontend e backend será feita via requisições HTTP utilizando dados no formato JSON.

---

## 📂 Estrutura do Projeto

```text
MedPet/
│
├── backend/                  # API Rest com FastAPI
│   ├── app/
│   │   ├── core/             # Configurações e segurança do sistema
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── dependencies.py
│   │   ├── models/           # Tabelas do banco de dados (SQLAlchemy)
│   │   │   ├── __init__.py
│   │   │   ├── atendimento.py
│   │   │   ├── cliente.py
│   │   │   ├── pet.py
│   │   │   └── usuario.py
│   │   ├── repositories/     # Operações no banco de dados
│   │   │   ├── __init__.py
│   │   │   ├── atendimento_repository.py
│   │   │   ├── cliente_repository.py
│   │   │   ├── pet_repository.py
│   │   │   └── usuario_repository.py
│   │   ├── routes/           # Endpoints da API (Rotas)
│   │   │   ├── __init__.py
│   │   │   ├── auth_routes.py
│   │   │   ├── atendimento_routes.py
│   │   │   ├── cliente_routes.py
│   │   │   ├── pet_routes.py
│   │   │   └── usuario_routes.py
│   │   ├── schemas/          # Validação de dados (Pydantic)
│   │   │   ├── __init__.py
│   │   │   ├── auth_schema.py
│   │   │   ├── atendimento_schema.py
│   │   │   ├── cliente_schema.py
│   │   │   ├── pet_schema.py
│   │   │   └── usuario_schema.py
│   │   ├── services/         # Regras de negócio da aplicação
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   ├── atendimento_service.py
│   │   │   ├── cliente_service.py
│   │   │   ├── pet_service.py
│   │   │   └── usuario_service.py
│   │   ├── database.py       # Conexão e Sessão do Banco de Dados
│   │   └── main.py           # Ponto de entrada da API
│   │
│   ├── scripts/              # Scripts auxiliares e de povoamento
│   │   └── seed.py
│   │
│   ├── Dockerfile            # Dockerfile para containerização do Backend
│   └── requirements.txt      # Dependências do backend
│
├── frontend/                 # Interface Web com Streamlit
│   ├── app.py                # Ponto de entrada do Frontend
│   ├── Dockerfile            # Dockerfile para containerização do Frontend
│   └── requirements.txt      # Dependências do frontend
│
├── tests/                    # Pasta raiz de testes automatizados
│   ├── __init__.py           # Inicializador de módulo de testes
│   ├── conftest.py           # Fixtures e configurações globais do Pytest
│   ├── api/                  # Testes integrados da API
│   │   └── __init__.py
│   ├── ui/                   # Testes de interface visual
│   │   └── __init__.py
│   └── unit/                 # Testes unitários de serviços e regras
│       └── __init__.py
│
├── docs/                     # Documentação de modelagem e requisitos
│   ├── diagramas/            # Modelagens UML (Usecase, Class, etc.)
│   ├── casos-de-uso.md
│   ├── requisitos.md
│   └── roteiro-apresentacao.md
│
├── .github/                  # Configurações do GitHub Actions (CI/CD)
│   └── workflows/
│       └── ci.yml            # Pipeline de integração contínua (testes e linting)
│
├── .env.example              # Exemplo de variáveis de ambiente configuráveis
├── .gitignore
├── docker-compose.yml        # Configuração para containers Docker
├── requirements-dev.txt      # Dependências do ambiente de desenvolvimento
└── README.md                 # Documentação principal do projeto
```

---

## 🔗 Principais Endpoints da API

### Autenticação
```http
POST /auth/login
POST /auth/register
```

### Clientes
```http
GET    /clientes
POST   /clientes
GET    /clientes/{id}
PUT    /clientes/{id}
DELETE /clientes/{id}
```

### Pets
```http
GET    /pets
POST   /pets
GET    /pets/{id}
PUT    /pets/{id}
DELETE /pets/{id}
```

### Atendimentos
```http
GET    /atendimentos
POST   /atendimentos
GET    /atendimentos/{id}
PUT    /atendimentos/{id}
DELETE /atendimentos/{id}
```

---

## 🧩 Padrões de Projeto Aplicados

### MVC Adaptado
Separação entre interface, rotas, regras de negócio e modelos.

### Repository
Isolamento da lógica de acesso ao banco de dados.

### Service Layer
Separação das regras de negócio em serviços específicos.

---

## 🧪 Testes

Os testes serão realizados de duas formas:

### Testes Manuais
- Validação dos endpoints pela documentação Swagger;
- Testes de cadastro, edição, listagem e exclusão;
- Verificação do fluxo entre Streamlit e FastAPI.

### Testes Automatizados
- Testes com Pytest para validar os principais endpoints;
- Verificação de respostas esperadas;
- Testes de erros, como registros inexistentes ou dados inválidos.

Exemplos de cenários:

| ID | Cenário | Resultado Esperado |
|---|---|---|
| CT01 | Login com dados válidos | Usuário autenticado com sucesso |
| CT02 | Cadastro de cliente válido | Cliente salvo no banco |
| CT03 | Cadastro de pet sem tutor | Erro de validação |
| CT04 | Consulta de atendimentos | Lista de atendimentos retornada |

---

## ▶️ Como Executar o Projeto

> **Dica:** Para simplificar a execução em projetos acadêmicos e não se preocupar com conflitos, o passo a passo abaixo usa a instalação direta (sem criar ambiente virtual/venv), visando facilitar a inicialização. 

### 1. Clone o repositório

```bash
git clone https://github.com/GuiCodeLabs/MedPet.git
cd MedPet
```

### 2. Instale as dependências

Instale os pacotes necessários tanto do Backend quanto do Frontend:

```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

### 3. Execute o Backend (FastAPI)

No seu terminal, navegue para a pasta do backend e inicie o servidor:

```bash
cd backend
uvicorn app.main:app --reload
```

- **Acesso à API:** `http://localhost:8000`
- **Documentação Swagger:** `http://localhost:8000/docs`

### 4. Execute o Frontend (Streamlit)

Abra um **novo terminal** (mantenha a aba anterior com o backend rodando), navegue para a pasta frontend e inicie a interface:

```bash
cd frontend
streamlit run app.py
```

- **Acesso à Interface Web:** `http://localhost:8501`

### 5. Execute os Testes Automatizados (Opcional)

Com a estrutura de testes na raiz do projeto, você pode executar as checagens e testes usando as dependências de desenvolvimento:

```bash
# Instale as dependências de desenvolvimento
pip install -r requirements-dev.txt

# Execute os testes com PYTHONPATH apontando para a pasta backend
PYTHONPATH=backend pytest tests/
```

---

## 👨‍💻 Divisão da Equipe

A divisão das tarefas foi pensada para que todos possam participar do planejamento, backend e frontend:

| Integrante | Papel e Responsabilidades Principais |
| :--- | :--- |
| **Guilherme** | Backend base, estrutura do banco de dados e autenticação |
| **Arllan** | Módulos de tutores, pets e diagramas UML |
| **Pedro H.** | Frontend Streamlit e integração com a API |
| **Pedro Antonio**| Consultas, prontuários, relatórios, testes e documentação/README |

---

## 📄 Documentação do Projeto

A documentação detalhada do projeto está organizada na pasta `docs/`.

| Documento | Descrição |
|---|---|
| [`requisitos.md`](docs/requisitos.md) | Apresenta os requisitos funcionais, não funcionais, regras de negócio e entidades principais do sistema. |
| [`casos-de-uso.md`](docs/casos-de-uso.md) | Descreve os atores do sistema, casos de uso e fluxos principais. |
| [`roteiro-apresentacao.md`](docs/roteiro-apresentacao.md) | Contém o roteiro resumido para a apresentação do projeto. |
| `diagramas/` | Pasta destinada aos diagramas UML do sistema. |

---

## 🚀 Roadmap

### Versão Inicial
- [x] Definição do tema do projeto;
- [x] Definição do escopo básico;
- [x] Estruturação do README;
- [ ] Criação dos diagramas UML;
- [ ] Implementação do backend;
- [ ] Implementação do frontend;
- [ ] Integração entre API e interface;
- [ ] Testes básicos;
- [ ] Deploy ou demonstração local.

### Melhorias Futuras
- [ ] Controle de estoque de medicamentos;
- [ ] Controle de vacinas;
- [ ] Relatórios avançados;
- [ ] Módulo financeiro;
- [ ] Notificações para tutores;
- [ ] Integração com WhatsApp;
- [ ] Deploy em nuvem.

---

## 📚 Referências

- Documentação oficial do FastAPI;
- Documentação oficial do Streamlit;
- SQLAlchemy ORM;
- Material da disciplina de Análise e Projeto de Sistemas;
- Conceitos de UML e Engenharia de Software.

---

## 👥 Equipe

Projeto desenvolvido por:

- Guilherme;
- Arllan;
- Pedro H.;
- Pedro Antonio.

---

## 📌 Status do Projeto

🚧 Em fase de planejamento e estruturação do escopo.

---

## 🐾 MedPet

Sistema simples, organizado e funcional para apoiar a gestão básica de uma clínica veterinária.
