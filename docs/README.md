# 📂 Documentação do Sistema — MedPet

Bem-vindo à documentação oficial do **MedPet**! Este diretório centraliza todas as especificações, modelos, roteiros e arquiteturas relativos ao sistema de gestão de clínica veterinária.

O objetivo desta documentação é facilitar a compreensão do sistema, o desenvolvimento de novas funcionalidades, a manutenção do código e a preparação para a apresentação acadêmica e prática do projeto.

> [!TIP]
> **Como visualizar os diagramas localmente:**
> Se você estiver usando o **VS Code**, instale a extensão **Markdown Preview Mermaid Support** ou **Mermaid Preview** para renderizar os diagramas UML diretamente na visualização do Markdown (`Ctrl + Shift + V`). Eles também são renderizados de forma nativa no GitHub.

---

## 🗺️ Mapa da Documentação

Para navegar entre os documentos detalhados de cada tópico do sistema, utilize o índice abaixo:

| Documento | Descrição |
| :--- | :--- |
| [📋 Requisitos](requisitos.md) | Lista de requisitos funcionais (RFs), requisitos não funcionais (RNFs) e regras de negócio (RNs) do sistema. |
| [👥 Casos de Uso](casos-de-uso.md) | Detalhamento dos atores, casos de uso (UCs) e fluxos de interação com o sistema. |
| [🏗️ Arquitetura](arquitetura.md) | Descrição das camadas do sistema (Frontend, Backend, Database) e padrões de projeto aplicados. |
| [🗄️ Modelo de Dados](modelo-dados.md) | Estruturação e detalhes físicos das tabelas do banco de dados relacional (SQLite). |
| [🔌 Documentação da API](api.md) | Lista de endpoints expostos pelo backend, parâmetros de requisição e modelos de resposta. |
| [🧪 Estratégia de Testes](testes.md) | Organização de testes automatizados (Pytest) e instruções para execução. |
| [⚙️ Integração Contínua (CI/CD)](ci-cd.md) | Funcionamento da automação de testes e checagem de código com GitHub Actions. |
| [🎤 Roteiro de Apresentação](roteiro-apresentacao.md) | Guia estruturado para apresentação e validação acadêmica do projeto. |
| [🎨 Diagramas (Pasta)](diagramas/) | Pasta física que armazena os arquivos-fonte `.mmd` dos diagramas UML de modelagem. |

---

## 📊 Matriz de Artefatos UML e Modelagem

Esta tabela sumariza todos os diagramas disponíveis para o sistema, indicando o tipo de modelagem e seu foco:

| Código | Diagrama | Tipo | Foco Principal | Arquivo de Origem |
| :---: | :--- | :--- | :--- | :--- |
| **UML-01** | [Casos de Uso](#1-diagrama-de-casos-de-uso) | Comportamental | Relação dos atores com as funcionalidades do sistema | [diagrama-casos-de-uso.mmd](diagramas/mermaids/diagrama-casos-de-uso.mmd) |
| **UML-02** | [Diagrama de Classes](#2-diagrama-de-classes) | Estrutural | Estruturação lógica e assinaturas das classes e entidades | [diagrama-classes.mmd](diagramas/mermaids/diagrama-classes.mmd) |
| **UML-03** | [Sequência (Login)](#3-diagrama-de-sequência---login) | Comportamental/Interação | Fluxo temporal e autenticação baseada em tokens JWT | [diagrama-sequencia-login.mmd](diagramas/mermaids/diagrama-sequencia-login.mmd) |
| **UML-04** | [Sequência (Atendimento)](#4-diagrama-de-sequência---registro-de-atendimento) | Comportamental/Interação | Passos para persistência e validação de consultas clínicas | [diagrama-sequencia-atendimento.mmd](diagramas/mermaids/diagrama-sequencia-atendimento.mmd) |
| **UML-05** | [Diagrama de Atividades](#5-diagrama-de-atividades) | Comportamental | Fluxo de processos de negócio de check-in e triagem de pets | [diagrama-atividades.mmd](diagramas/mermaids/diagrama-atividades.mmd) |
| **UML-06** | [Componentes](#6-diagrama-de-componentes) | Estrutural | Camadas físicas e dependências lógicas (Streamlit / FastAPI / DB) | [diagrama-componentes.mmd](diagramas/mermaids/diagrama-componentes.mmd) |
| **UML-07** | [Modelo Relacional (ERD)](#7-diagrama-de-entidade-relacionamento-erd) | Estrutural (Dados) | Modelagem física das tabelas SQLite e chaves PK/FK | [diagrama-entidade-relacionamento.mmd](diagramas/mermaids/diagrama-entidade-relacionamento.mmd) |

---

## 🛠️ Como contribuir para a Documentação e Diagramas

Para manter a consistência da documentação do MedPet, siga as diretrizes abaixo:

1. **Clareza e Precisão**: Use termos claros e padronizados conforme o domínio (ex: tutor/cliente, pet, atendimento).
2. **Sincronização com o Código**: Sempre que houver mudanças em modelos do banco de dados, endpoints de rotas ou regras de negócio, os arquivos Markdown correspondentes nesta pasta devem ser atualizados.
3. **Padrão dos Diagramas**:
   - Salve novos diagramas na pasta `diagramas/mermaids/` com a extensão `.mmd`.
   - Lembre-se de atualizar tanto o arquivo `.mmd` isolado quanto o bloco inline embutido neste `README.md`.
4. **Boas Práticas de Sintaxe Mermaid**:
   - > [!WARNING]
     > **Atenção aos parênteses:** Parênteses contidos em labels de conexões como `Client -->|Requisições (JSON)| Routes` causam erros de parsing no Mermaid, pois o parser os confunde com a sintaxe de formato dos nós (nós arredondados). Sempre utilize aspas duplas nas labels se houver caracteres especiais ou parênteses, por exemplo: `Client -->|"Requisições (JSON)"| Routes`.

---

---

## 📊 Diagramas Visuais do Sistema (UML e Modelagem)

Esta seção exibe a renderização em tempo real de todos os diagramas do **MedPet** utilizando sintaxe Mermaid. Você também pode acessar e editar os arquivos de código-fonte originais clicando nos links fornecidos.

### 👥 1. Diagrama de Casos de Uso
Descreve as interações dos atores (Administrador, Funcionário e Veterinário) com as funcionalidades centrais do sistema.
> 🔗 **Fonte:** [diagrama-casos-de-uso.mmd](diagramas/mermaids/diagrama-casos-de-uso.mmd)

```mermaid
flowchart LR
    %% ── Atores ──
    admin["👤 Administrador"]
    func["👤 Funcionário"]
    vet["👤 Veterinário"]

    %% ── Ordem vertical dos atores ──
    admin ~~~ func ~~~ vet

    %% ── Módulos do Sistema ──
    subgraph S1["🔐 Autenticação"]
        uc01("UC01 · Realizar Login")
        uc02("UC02 · Cadastrar Usuário")
    end

    subgraph S2["👥 Gestão de Clientes"]
        uc03("UC03 · Cadastrar Cliente")
        uc04("UC04 · Consultar Cliente")
        uc05("UC05 · Atualizar Cliente")
        uc06("UC06 · Excluir Cliente")
    end

    subgraph S3["🐾 Gestão de Pets"]
        uc07("UC07 · Cadastrar Pet")
        uc08("UC08 · Consultar Pet")
        uc09("UC09 · Atualizar Pet")
        uc10("UC10 · Excluir Pet")
    end

    subgraph S4["🩺 Atendimentos"]
        uc11("UC11 · Registrar Atendimento")
        uc12("UC12 · Consultar Atendimento")
    end

    %% ── Administrador — acesso total ──
    admin --> uc01 & uc02
    admin --> uc03 & uc04 & uc05 & uc06
    admin --> uc07 & uc08 & uc09 & uc10
    admin --> uc11 & uc12

    %% ── Funcionário ──
    func --> uc01
    func --> uc03 & uc04 & uc05
    func --> uc07 & uc08 & uc09
    func --> uc12

    %% ── Veterinário ──
    vet --> uc01
    vet --> uc04
    vet --> uc08 & uc09
    vet --> uc11 & uc12

    %% ── Estilos ──
    classDef actorStyle fill:#4A90D9,stroke:#2C5F8A,color:#FFFFFF,font-weight:bold,rx:12,ry:12
    classDef authStyle fill:#6C5CE7,stroke:#4834D4,color:#FFFFFF,rx:8,ry:8
    classDef clienteStyle fill:#00B894,stroke:#00896A,color:#FFFFFF,rx:8,ry:8
    classDef petStyle fill:#FDCB6E,stroke:#E17E00,color:#2D3436,rx:8,ry:8
    classDef atendStyle fill:#E17055,stroke:#B33939,color:#FFFFFF,rx:8,ry:8

    class admin,func,vet actorStyle
    class uc01,uc02 authStyle
    class uc03,uc04,uc05,uc06 clienteStyle
    class uc07,uc08,uc09,uc10 petStyle
    class uc11,uc12 atendStyle
```

---

### 🧱 2. Diagrama de Classes
Apresenta o mapeamento estático das entidades de modelo (Usuario, Cliente, Pet, Atendimento) e a estrutura lógica das classes de serviço.
> 🔗 **Fonte:** [diagrama-classes.mmd](diagramas/mermaids/diagrama-classes.mmd)

```mermaid
classDiagram
    direction TB

    %% Entidades de Modelos (Entidades SQLAlchemy)
    class Usuario {
        +int id
        +string nome
        +string email
        +string senha_hash
        +string perfil
        +boolean ativo
        +datetime criado_em
    }

    class Cliente {
        +int id
        +string nome
        +string cpf
        +string email
        +string telefone
        +string endereco
        +datetime criado_em
        +list~Pet~ pets
    }

    class Pet {
        +int id
        +string nome
        +string especie
        +string raca
        +int idade
        +float peso
        +int cliente_id
        +datetime criado_em
        +Cliente dono
        +list~Atendimento~ atendimentos
    }

    class Atendimento {
        +int id
        +string motivo
        +string descricao
        +int pet_id
        +datetime data
        +Pet pet
    }

    %% Serviços
    class UsuarioService {
        -Session db
        +create(UsuarioCreate user_in) Usuario
        +list_all() list~Usuario~
    }

    class ClienteService {
        -Session db
        +create(ClienteCreate cliente_in) Cliente
        +list_all() list~Cliente~
        +get_by_id(int id) Cliente
    }

    class PetService {
        -Session db
        +create(PetCreate pet_in) Pet
        +list_all() list~Pet~
        +list_by_owner(int cliente_id) list~Pet~
    }

    class AtendimentoService {
        -Session db
        +create(AtendimentoCreate atendimento_in) Atendimento
        +list_all() list~Atendimento~
        +list_by_pet(int pet_id) list~Atendimento~
    }

    %% Relacionamentos de Entidades
    Cliente "1" --> "0..*" Pet : "dono de"
    Pet "1" --> "0..*" Atendimento : "recebe"

    %% Relacionamentos com os Serviços (Dependências / Chamadas)
    UsuarioService ..> Usuario : "manipula"
    ClienteService ..> Cliente : "manipula"
    PetService ..> Pet : "manipula"
    AtendimentoService ..> Atendimento : "manipula"
```

---

### 🔑 3. Diagrama de Sequência — Login
Ilustra a troca de mensagens na autenticação do operador (Atendente/Vet/Admin), com hash de senhas e geração de Token JWT.
> 🔗 **Fonte:** [diagrama-sequencia-login.mmd](diagramas/mermaids/diagrama-sequencia-login.mmd)

```mermaid
sequenceDiagram
    autonumber
    actor Operador as 👤 Operador (Atendente/Vet/Admin)
    participant Streamlit as 💻 Streamlit (Frontend)
    participant FastAPI as 🚀 FastAPI (Route /auth/login)
    participant Service as ⚙️ AuthService
    participant Repo as 🗄️ UsuarioRepository
    participant DB as 💾 Banco de Dados (SQLite)

    Operador->>Streamlit: Insere e-mail e senha e clica em Login
    Streamlit->>FastAPI: POST /auth/login { username, password }
    FastAPI->>Service: authenticate_user(login_request)
    Service->>Repo: get_by_email(username)
    Repo->>DB: SELECT * FROM usuarios WHERE email = username
    DB-->>Repo: Retorna dados do Usuário (id, nome, senha_hash)
    Repo-->>Service: Retorna objeto Usuario
    
    alt Usuário existe e senha_hash é válida (bcrypt)
        Service->>Service: Gerar Token JWT com claims (id, email, perfil)
        Service-->>FastAPI: Retorna { access_token, token_type: "bearer" }
        FastAPI-->>Streamlit: HTTP 200 OK com Token JSON
        Streamlit->>Streamlit: Salva Token na Session State
        Streamlit-->>Operador: Exibe "Login realizado com sucesso!" e redireciona
    else Credenciais inválidas / Usuário não encontrado
        Service-->>FastAPI: Retorna None
        FastAPI-->>Streamlit: HTTP 401 Unauthorized { "detail": "E-mail ou senha incorretos." }
        Streamlit-->>Operador: Exibe mensagem de erro na interface
    end
```

---

### 🩺 4. Diagrama de Sequência — Registro de Atendimento
Exibe o fluxo completo de registro de consulta veterinária, com verificações de consistência cadastral do animal.
> 🔗 **Fonte:** [diagrama-sequencia-atendimento.mmd](diagramas/mermaids/diagrama-sequencia-atendimento.mmd)

```mermaid
sequenceDiagram
    autonumber
    actor VetAdmin as 👤 Veterinário / Administrador
    participant Streamlit as 💻 Streamlit (Frontend)
    participant FastAPI as 🚀 FastAPI (Route /atendimentos/)
    participant Service as ⚙️ AtendimentoService
    participant PetRepo as 🗄️ PetRepository
    participant AtendRepo as 🗄️ AtendimentoRepository
    participant DB as 💾 Banco de Dados (SQLite)

    VetAdmin->>Streamlit: Insere dados (motivo, descrição, pet_id) e clica em Salvar
    Streamlit->>FastAPI: POST /atendimentos/ { motivo, descricao, pet_id }
    FastAPI->>Service: create(atendimento_in)
    Service->>PetRepo: get_by_id(pet_id)
    PetRepo->>DB: SELECT * FROM pets WHERE id = pet_id
    DB-->>PetRepo: Retorna dados do Pet (ou None)
    PetRepo-->>Service: Retorna objeto Pet (ou None)

    alt Pet não cadastrado no banco de dados
        Service-->>FastAPI: Lança ValueError("Pet não encontrado")
        FastAPI-->>Streamlit: HTTP 400 Bad Request { "detail": "Pet não encontrado." }
        Streamlit-->>VetAdmin: Exibe aviso de erro na tela
    else Pet cadastrado com sucesso
        Service->>AtendRepo: create(novo_atendimento_model)
        AtendRepo->>DB: INSERT INTO atendimentos (motivo, descricao, pet_id)
        DB-->>AtendRepo: Retorna objeto salvo com id e data gerados
        AtendRepo-->>Service: Retorna objeto Atendimento
        Service-->>FastAPI: Retorna objeto Atendimento
        FastAPI-->>Streamlit: HTTP 201 Created com AtendimentoResponse
        Streamlit-->>VetAdmin: Exibe toast "Atendimento registrado com sucesso!"
    end
```

---

### 🔄 5. Diagrama de Atividades
Representa o fluxo lógico de negócio na clínica veterinária para o check-in de tutores, cadastro de animais e registro de consultas.
> 🔗 **Fonte:** [diagrama-atividades.mmd](diagramas/mermaids/diagrama-atividades.mmd)

```mermaid
stateDiagram-v2
    [*] --> Recepcao

    state Recepcao {
        [*] --> ReceberCliente : Receber Cliente e Pet na recepção
        ReceberCliente --> VerificarTutor : Verificar se Tutor (Cliente) já possui cadastro
    }

    state VerificarTutor <<choice>>
    VerificarTutor --> CadastrarTutor : Não
    VerificarTutor --> VerificarPet : Sim

    state CadastrarTutor {
        [*] --> FormTutor : Preencher Nome, CPF, E-mail, Telefone e Endereço
        FormTutor --> SalvarTutorAPI : Enviar POST /clientes/
        SalvarTutorAPI --> TutorCadastrado : Retorno 201 Created do Backend
    }

    TutorCadastrado --> VerificarPet

    state VerificarPet <<choice>>
    VerificarPet --> CadastrarPet : Não
    VerificarPet --> RegistrarAtendimento : Sim

    state CadastrarPet {
        [*] --> FormPet : Preencher Nome, Espécie, Raça, Idade e Peso
        FormPet --> AssociarTutor : Vincular ao ID do Tutor cadastrado
        AssociarTutor --> SalvarPetAPI : Enviar POST /pets/
        SalvarPetAPI --> PetCadastrado : Retorno 201 Created do Backend
    }

    PetCadastrado --> RegistrarAtendimento

    state RegistrarAtendimento {
        [*] --> FormAtendimento : Informar Motivo (Consulta/Vacina) e Observações Clínicas
        FormAtendimento --> VincularPet : Vincular ao ID do Pet selecionado
        VincularPet --> SalvarAtendimentoAPI : Enviar POST /atendimentos/
        SalvarAtendimentoAPI --> AtendimentoRegistrado : Retorno 201 Created do Backend
    }

    AtendimentoRegistrado --> [*]
```

---

### 📦 6. Diagrama de Componentes
Demonstra a arquitetura lógica em camadas da nossa stack unificada em Python.
> 🔗 **Fonte:** [diagrama-componentes.mmd](diagramas/mermaids/diagrama-componentes.mmd)

```mermaid
flowchart TD
    subgraph Frontend["💻 Camada de Apresentação (Streamlit Frontend)"]
        UI["Tela Web (app.py)"]
        Client["Cliente de Integração HTTP (requests)"]
        UI --> Client
    end

    subgraph Backend["🚀 Camada de Negócio (FastAPI Backend)"]
        subgraph Routes["🔌 API Controllers (Routes)"]
            AuthRoutes["auth_routes.py"]
            UserRoutes["usuario_routes.py"]
            ClientRoutes["cliente_routes.py"]
            PetRoutes["pet_routes.py"]
            AtendRoutes["atendimento_routes.py"]
        end

        subgraph Core["⚙️ Core & Segurança"]
            Sec["security.py (JWT / bcrypt)"]
            Deps["dependencies.py (get_db / get_current_user)"]
        end

        subgraph Services["🧬 Camada de Serviço (Services)"]
            AuthService["auth_service.py"]
            UserService["usuario_service.py"]
            ClienteService["cliente_service.py"]
            PetService["pet_service.py"]
            AtendimentoService["atendimento_service.py"]
        end

        subgraph Repos["🗄️ Camada de Persistência (Repositories)"]
            UserRepo["usuario_repository.py"]
            ClienteRepo["cliente_repository.py"]
            PetRepo["pet_repository.py"]
            AtendRepo["atendimento_repository.py"]
        end
    end

    subgraph Database["💾 Banco de Dados"]
        SQLiteDB[("clinica_veterinaria.db (SQLite)")]
    end

    %% Relações do Frontend
    Client -->|"Requisições HTTP REST (JSON)"| Routes

    %% Relações dos Routes
    AuthRoutes --> AuthService
    UserRoutes --> UserService
    ClientRoutes --> ClienteService
    PetRoutes --> PetService
    AtendRoutes --> AtendimentoService
    
    Routes -.->|Valida tokens| Deps
    Deps -.->|Injeta decodificação JWT| Sec

    %% Relações dos Services
    AuthService --> UserRepo
    UserService --> UserRepo
    ClienteService --> ClienteRepo
    PetService --> PetRepo
    AtendimentoService --> AtendRepo
    AtendimentoService --> PetRepo

    %% Relações dos Repositories
    UserRepo -->|SQLAlchemy ORM| SQLiteDB
    ClienteRepo -->|SQLAlchemy ORM| SQLiteDB
    PetRepo -->|SQLAlchemy ORM| SQLiteDB
    AtendRepo -->|SQLAlchemy ORM| SQLiteDB
```

---

### 🗄️ 7. Diagrama de Entidade-Relacionamento (ERD)
Representa o design e propriedades das tabelas do banco de dados relacional.
> 🔗 **Fonte:** [diagrama-entidade-relacionamento.mmd](diagramas/mermaids/diagrama-entidade-relacionamento.mmd)

```mermaid
erDiagram
    usuarios {
        int id PK
        string nome "VARCHAR(100) NOT NULL"
        string email UK "VARCHAR(120) NOT NULL"
        string senha_hash "VARCHAR(255) NOT NULL"
        string perfil "VARCHAR(30) NOT NULL"
        boolean ativo "BOOLEAN NOT NULL"
        datetime criado_em "DATETIME NOT NULL"
    }

    clientes {
        int id PK
        string nome "VARCHAR(100) NOT NULL"
        string cpf UK "VARCHAR(14) NOT NULL"
        string email UK "VARCHAR(120) NOT NULL"
        string telefone "VARCHAR(20) NULL"
        string endereco "VARCHAR(200) NULL"
        datetime criado_em "DATETIME NOT NULL"
    }

    pets {
        int id PK
        string nome "VARCHAR(50) NOT NULL"
        string especie "VARCHAR(30) NOT NULL"
        string raca "VARCHAR(50) NULL"
        int idade "INTEGER NULL"
        float peso "FLOAT NULL"
        int cliente_id FK "INTEGER NOT NULL"
        datetime criado_em "DATETIME NOT NULL"
    }

    atendimentos {
        int id PK
        string motivo "VARCHAR(100) NOT NULL"
        string descricao "VARCHAR(500) NULL"
        int pet_id FK "INTEGER NOT NULL"
        datetime data "DATETIME NOT NULL"
    }

    %% Relacionamentos
    clientes ||--o{ pets : "possui"
    pets ||--o{ atendimentos : "recebe"
```

