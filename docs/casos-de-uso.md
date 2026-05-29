# 👥 Casos de Uso — MedPet

## 1. Visão Geral

Este documento detalha os **Casos de Uso (UCs)** do sistema **MedPet**, especificando os fluxos lógicos e interações entre os atores operacionais e a aplicação clínica. 

Os casos de uso servem como contrato de desenvolvimento para a interface do frontend (Streamlit) e são validados de forma automatizada pelos testes de integração da API.

---

## 2. Atores do Sistema

O sistema conta com três perfis de usuários com diferentes privilégios de acesso:

* **Administrador (Admin)**: Acesso irrestrito a todas as operações, incluindo criação de operadores do sistema e exclusões de registros históricos de clientes, pets ou consultas.
* **Funcionário (Atendente)**: Focado em atividades administrativas da recepção, como cadastro de clientes e pets, e consulta de históricos.
* **Veterinário (Vet)**: Focado na parte clínica, com autorização para consultar dados de prontuários e registrar novos atendimentos clínicos.

---

## 3. Matriz de Casos de Uso

| Código | Caso de Uso | Atores Principais | Permissão Mínima | Link de Detalhe |
| :---: | :--- | :--- | :---: | :--- |
| **UC01** | Realizar login | Administrador, Funcionário, Veterinário | Qualquer perfil | [Detalhar UC01](#uc01--realizar-login) |
| **UC02** | Cadastrar usuário | Administrador | Administrador | [Detalhar UC02](#uc02--cadastrar-usuario) |
| **UC03** | Cadastrar cliente | Administrador, Funcionário | Funcionário | [Detalhar UC03](#uc03--cadastrar-cliente) |
| **UC04** | Consultar cliente | Administrador, Funcionário, Veterinário | Qualquer perfil | [Detalhar UC04](#uc04--consultar-cliente) |
| **UC05** | Atualizar cliente | Administrador, Funcionário | Funcionário | [Detalhar UC05](#uc05--atualizar-cliente) |
| **UC06** | Excluir cliente | Administrador | Administrador | [Detalhar UC06](#uc06--excluir-cliente) |
| **UC07** | Cadastrar pet | Administrador, Funcionário | Funcionário | [Detalhar UC07](#uc07--cadastrar-pet) |
| **UC08** | Consultar pet | Administrador, Funcionário, Veterinário | Qualquer perfil | [Detalhar UC08](#uc08--consultar-pet) |
| **UC09** | Atualizar pet | Administrador, Funcionário, Veterinário | Qualquer perfil | [Detalhar UC09](#uc09--atualizar-pet) |
| **UC10** | Excluir pet | Administrador | Administrador | [Detalhar UC10](#uc10--excluir-pet) |
| **UC11** | Registrar atendimento | Administrador, Veterinário | Veterinário | [Detalhar UC11](#uc11--registrar-atendimento) |
| **UC12** | Consultar atendimento | Administrador, Funcionário, Veterinário | Qualquer perfil | [Detalhar UC12](#uc12--consultar-atendimento) |

---

## 4. Detalhamento dos Casos de Uso

### UC01 — Realizar Login

* **Atores**: Administrador, Funcionário ou Veterinário.
* **Objetivo**: Permitir que o operador se autentique no sistema.
* **Pré-condições**: Conta de usuário ativa no banco de dados.
* **Entradas**: E-mail e senha.
* **Saídas**: Token de acesso JWT (guardado no Session State) e liberação de acesso.

| Passo | Ação do Ator | Resposta do Sistema |
| :---: | :--- | :--- |
| **1** | Insere e-mail e senha na tela de login. | Valida se os campos foram preenchidos. |
| **2** | Clica no botão "Entrar". | Envia os dados para a rota `/auth/login` e verifica o hash da senha via bcrypt. |
| **3** | | Gera o Token JWT e redireciona o usuário à página inicial. |

> [!WARNING]
> **Fluxo de Exceção (Credenciais Inválidas):** Caso o e-mail não seja encontrado ou a senha esteja incorreta, o sistema retorna `HTTP 401 Unauthorized` e o frontend exibe o aviso "E-mail ou senha incorretos".

---

### UC02 — Cadastrar Usuário

* **Atores**: Administrador.
* **Objetivo**: Adicionar um novo operador com privilégios específicos ao sistema.
* **Pré-condições**: Administrador autenticado no sistema.
* **Entradas**: Nome, e-mail, senha de acesso inicial, perfil (Administrador, Funcionário ou Veterinário).
* **Saídas**: Confirmação de cadastro do usuário.

> [!CAUTION]
> **Privilégio Exclusivo:** Apenas administradores conseguem criar outras contas de operadores no sistema.

| Passo | Ação do Ator | Resposta do Sistema |
| :---: | :--- | :--- |
| **1** | Acessa a aba "Gerenciar Usuários" e preenche o formulário. | Exibe formulário contendo campo de Perfil como caixa de seleção (Selectbox). |
| **2** | Clica em "Salvar Usuário". | Envia `POST /usuarios/`, valida campos, criptografa a senha e salva na base de dados. |

---

### UC03 — Cadastrar Cliente

* **Atores**: Administrador ou Funcionário.
* **Objetivo**: Cadastrar o tutor responsável pelos animais atendidos na clínica.
* **Pré-condições**: Operador autenticado.
* **Entradas**: Nome completo, CPF, E-mail, Telefone e Endereço.
* **Saídas**: Cliente salvo com ID gerado automaticamente.

| Passo | Ação do Ator | Resposta do Sistema |
| :---: | :--- | :--- |
| **1** | Acessa a aba "Clientes" e escolhe "Novo Cadastro". | Exibe formulário limpo. |
| **2** | Preenche os dados e clica em "Salvar". | Valida formato do CPF e e-mail. Salva o registro e retorna `HTTP 201 Created`. |

> [!NOTE]
> **Fluxo de Exceção (CPF Duplicado):** Se o CPF digitado já estiver cadastrado na tabela de clientes, o sistema retorna `HTTP 400 Bad Request` e a interface avisa que o cliente já existe.

---

### UC04 — Consultar Cliente

* **Atores**: Administrador, Funcionário ou Veterinário.
* **Objetivo**: Listar clientes e encontrar dados cadastrais de contato.
* **Pré-condições**: Operador autenticado.
* **Entradas**: Termo de busca (Nome ou CPF do cliente).
* **Saídas**: Lista de registros correspondentes.

---

### UC05 — Atualizar Cliente

* **Atores**: Administrador ou Funcionário.
* **Objetivo**: Corrigir ou atualizar o cadastro do tutor (telefone, endereço, etc.).
* **Pré-condições**: Operador autenticado e cliente selecionado.
* **Entradas**: Novos dados do cliente.
* **Saídas**: Mensagem "Cadastro atualizado com sucesso".

---

### UC06 — Excluir Cliente

* **Atores**: Administrador.
* **Objetivo**: Remover um cliente do banco de dados da clínica.
* **Pré-condições**: Administrador autenticado.
* **Entradas**: Confirmação de exclusão.
* **Saídas**: Remoção em cascata dos registros.

> [!CAUTION]
> **Aviso de Cascata:** A exclusão de um cliente remove automaticamente todos os seus pets e históricos de atendimento associados do banco de dados devido à integridade referencial.

---

### UC07 — Cadastrar Pet

* **Atores**: Administrador ou Funcionário.
* **Objetivo**: Cadastrar um animal e associá-lo a um tutor cadastrado.
* **Pré-condições**: Tutor (Cliente) deve estar previamente cadastrado.
* **Entradas**: Nome do animal, espécie (selectbox), raça, idade, peso e tutor responsável.
* **Saídas**: Pet registrado e vinculado ao ID do cliente.

---

### UC08 — Consultar Pet

* **Atores**: Administrador, Funcionário ou Veterinário.
* **Objetivo**: Pesquisar animais por nome ou pelo nome do tutor.
* **Pré-condições**: Pet registrado na base.
* **Entradas**: Nome do pet ou tutor.
* **Saídas**: Detalhes do animal e identificação do dono.

---

### UC09 — Atualizar Pet

* **Atores**: Administrador, Funcionário ou Veterinário.
* **Objetivo**: Atualizar o peso, idade ou raça do animal após uma nova consulta.
* **Pré-condições**: Pet selecionado na listagem.

---

### UC10 — Excluir Pet

* **Atores**: Administrador.
* **Objetivo**: Remover permanentemente o cadastro de um animal.

> [!CAUTION]
> **Privilégio Exclusivo:** Apenas o Administrador pode excluir um pet, o que acarreta a exclusão automática de todo o seu histórico clínico (atendimentos).

---

### UC11 — Registrar Atendimento

* **Atores**: Administrador ou Veterinário.
* **Objetivo**: Lançar dados da consulta clínica do animal, medicamentos e observações.
* **Pré-condições**: Pet previamente cadastrado no banco.
* **Entradas**: Pet selecionado, motivo (Consulta, Vacina, Cirurgia), descrição detalhada.
* **Saídas**: Atendimento gravado com data e hora automática.

| Passo | Ação do Ator | Resposta do Sistema |
| :---: | :--- | :--- |
| **1** | Seleciona o pet atendido na tela e preenche o prontuário. | Resgata informações básicas do pet. |
| **2** | Digita observações clínicas e clica em "Salvar". | Valida associação, cria data do sistema, persiste dados na tabela `atendimentos` e retorna `HTTP 201`. |

---

### UC12 — Consultar Atendimento

* **Atores**: Administrador, Funcionário ou Veterinário.
* **Objetivo**: Visualizar a lista de consultas da clínica ou o histórico clínico de um pet específico.
* **Pré-condições**: Atendimentos registrados.
* **Entradas**: Seleção do Pet ou busca global.
* **Saídas**: Exibição em tela das consultas com data, motivo e descrição.

---

## 5. Regras Lógicas de Sistema

1. **Autenticação**: O frontend impede o carregamento de abas internas se o token JWT não estiver na Session State do Streamlit.
2. **Cascata**: Excluir clientes aciona o cascade no SQLAlchemy apagando recursivamente pets e atendimentos.
3. **Consistência de Dados**: O peso de pets deve ser maior que zero; o CPF do cliente deve possuir 11 dígitos numéricos válidos.