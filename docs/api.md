# 🔌 Documentação da API REST — MedPet

Este documento detalha os endpoints da API REST do **MedPet**, especificando rotas, métodos HTTP, dados de entrada (Request Body) e esquemas de resposta.

---

## 1. Configurações e Segurança

* **URL Base**: `http://localhost:8000`
* **Formato**: `application/json` (para corpos de requisição e resposta).
* **Documentação Interativa (Swagger)**: Disponível localmente em `http://localhost:8000/docs` com a API em execução.

> [!IMPORTANT]
> **Cabeçalho de Autenticação JWT**
> Exceto para as rotas públicas de login e criação de usuários, todas as demais chamadas à API exigem o cabeçalho HTTP:
> `Authorization: Bearer <seu_token_jwt>`

---

## 2. Endpoints de Autenticação (`/auth`)

Rotas de login e geração de credenciais de sessão.

### 2.1. Realizar Login
* **Método/Rota**: `POST /auth/login`
* **Descrição**: Autentica e gera o Token JWT para uso nas demais requisições.
* **Corpo da Requisição (Request Body)**:
  ```json
  {
    "username": "usuario@email.com",
    "password": "senha_secreta"
  }
  ```
* **Formatos de Resposta**:
  * **`200 OK`**: Retorna as credenciais de sessão.
    ```json
    {
      "access_token": "eyJhbGciOiJIUzI1NiIsIn...",
      "token_type": "bearer"
    }
    ```
  * **`401 Unauthorized`**: Erro de credenciais.
    ```json
    {
      "detail": "E-mail ou senha incorretos."
    }
    ```

---

## 3. Endpoints de Usuários (`/usuarios`)

Rotas para gestão de operadores do sistema (protegidas por token JWT).

### 3.1. Cadastrar Usuário
* **Método/Rota**: `POST /usuarios/`
* **Descrição**: Registra um novo operador no banco de dados.
* **Corpo da Requisição**:
  ```json
  {
    "nome": "João da Silva",
    "email": "joao@email.com",
    "senha": "senha123_segura",
    "perfil": "atendente",
    "ativo": true
  }
  ```
* **Formatos de Resposta**:
  * **`201 Created`**: Usuário cadastrado.
    ```json
    {
      "nome": "João da Silva",
      "email": "joao@email.com",
      "perfil": "atendente",
      "ativo": true,
      "id": 1,
      "criado_em": "2026-05-26T22:30:00"
    }
    ```

### 3.2. Listar Usuários
* **Método/Rota**: `GET /usuarios/`
* **Descrição**: Recupera a lista com todas as contas de operadores.

---

## 4. Endpoints de Clientes (`/clientes`)

Rotas para a gestão cadastral de tutores (protegidas por token JWT).

### 4.1. Cadastrar Cliente
* **Método/Rota**: `POST /clientes/`
* **Descrição**: Adiciona um tutor à base.
* **Corpo da Requisição**:
  ```json
  {
    "nome": "Maria Souza",
    "cpf": "123.456.789-00",
    "email": "maria@email.com",
    "telefone": "(11) 98888-8888",
    "endereco": "Rua das Flores, 123"
  }
  ```
* **Formatos de Resposta**:
  * **`201 Created`**:
    ```json
    {
      "nome": "Maria Souza",
      "cpf": "123.456.789-00",
      "email": "maria@email.com",
      "telefone": "(11) 98888-8888",
      "endereco": "Rua das Flores, 123",
      "id": 1,
      "criado_em": "2026-05-26T22:35:00"
    }
    ```

### 4.2. Listar Clientes
* **Método/Rota**: `GET /clientes/`

### 4.3. Obter Detalhes de Cliente por ID
* **Método/Rota**: `GET /clientes/{id}`

---

## 5. Endpoints de Pets (`/pets`)

Rotas para gestão de animais de estimação (protegidas por token JWT).

### 5.1. Cadastrar Pet
* **Método/Rota**: `POST /pets/`
* **Descrição**: Registra um animal obrigatoriamente associado a um tutor existente (`cliente_id`).
* **Corpo da Requisição**:
  ```json
  {
    "nome": "Rex",
    "especie": "Cachorro",
    "raca": "Vira-lata",
    "idade": 3,
    "peso": 12.5,
    "cliente_id": 1
  }
  ```
* **Formatos de Resposta**:
  * **`201 Created`**:
    ```json
    {
      "nome": "Rex",
      "especie": "Cachorro",
      "raca": "Vira-lata",
      "idade": 3,
      "peso": 12.5,
      "cliente_id": 1,
      "id": 1,
      "criado_em": "2026-05-26T22:40:00"
    }
    ```

### 5.2. Listar Pets
* **Método/Rota**: `GET /pets/`

### 5.3. Listar Pets por Tutor
* **Método/Rota**: `GET /pets/tutor/{cliente_id}`

---

## 6. Endpoints de Atendimentos (`/atendimentos`)

Rotas para o histórico de consultas clínicas (protegidas por token JWT).

### 6.1. Registrar Atendimento
* **Método/Rota**: `POST /atendimentos/`
* **Descrição**: Lança um prontuário médico para um pet cadastrado.
* **Corpo da Requisição**:
  ```json
  {
    "motivo": "Vacina",
    "descricao": "Aplicação da vacina antirrábica anual.",
    "pet_id": 1
  }
  ```
* **Formatos de Resposta**:
  * **`201 Created`**:
    ```json
    {
      "motivo": "Vacina",
      "descricao": "Aplicação da vacina antirrábica anual.",
      "pet_id": 1,
      "id": 1,
      "data": "2026-05-26T22:45:00"
    }
    ```

### 6.2. Listar Atendimentos
* **Método/Rota**: `GET /atendimentos/`

### 6.3. Listar Atendimentos por Pet
* **Método/Rota**: `GET /atendimentos/pet/{pet_id}`
