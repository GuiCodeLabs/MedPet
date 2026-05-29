# 📋 Requisitos do Sistema — MedPet

## 1. Visão Geral

O **MedPet** é um sistema web voltado para a gestão básica de uma clínica veterinária. O objetivo do sistema é permitir o cadastro, consulta, atualização e exclusão de informações relacionadas a usuários, clientes, pets e atendimentos veterinários.

Este documento apresenta os **Requisitos Funcionais (RFs)**, **Requisitos Não Funcionas (RNFs)** e as **Regras de Negócio (RNs)** do sistema, servindo como a base de qualidade para o desenvolvimento do backend, da interface Streamlit e da suíte de testes do projeto.

---

## 2. Requisitos Funcionais

Os requisitos funcionais representam as funcionalidades diretas que o sistema deve oferecer aos usuários operadores (atendentes, veterinários e administradores).

| Código | Requisito | Descrição | Nível de Acesso |
| :---: | :--- | :--- | :--- |
| **RF01** | Cadastrar usuário | Permitir o cadastro de novos operadores do sistema com e-mail, nome, senha e perfil. | Administrador |
| **RF02** | Autenticar usuário | Permitir login via e-mail e senha com geração de Token JWT. | Todos os perfis |
| **RF03** | Cadastrar cliente | Registrar tutores de animais com CPF, e-mail, nome, telefone e endereço. | Administrador, Funcionário |
| **RF04** | Consultar clientes | Listar e pesquisar clientes/tutores cadastrados. | Todos os perfis |
| **RF05** | Atualizar cliente | Alterar dados cadastrais de um cliente existente. | Administrador, Funcionário |
| **RF06** | Excluir cliente | Remover permanentemente um cliente e seus pets associados. | Administrador |
| **RF07** | Cadastrar pet | Cadastrar um animal vinculando-o obrigatoriamente a um tutor (cliente). | Administrador, Funcionário |
| **RF08** | Consultar pets | Listar e pesquisar pets, visualizando sua espécie, raça, idade e peso. | Todos os perfis |
| **RF09** | Atualizar pet | Alterar dados cadastrais de um pet existente. | Todos os perfis |
| **RF10** | Excluir pet | Remover permanentemente um pet e seu histórico de consultas. | Administrador |
| **RF11** | Registrar atendimento | Registrar detalhes de uma consulta ou procedimento médico de um pet. | Administrador, Veterinário |
| **RF12** | Consultar atendimentos| Visualizar o histórico completo de atendimentos gerais ou filtrado por pet. | Todos os perfis |

---

## 3. Requisitos Não Funcionais

Os requisitos não funcionais especificam critérios que podem ser usados para julgar a operação de um sistema, em vez de comportamentos específicos.

| Código | Categoria | Descrição |
| :---: | :--- | :--- |
| **RNF01** | Segurança | Acesso autenticado via protocolo **OAuth2** com tokens **JWT** (JSON Web Tokens). |
| **RNF02** | Usabilidade | Interface construída com **Streamlit**, focando em simplicidade e fluxo intuitivo para o atendente/vet. |
| **RNF03** | Desempenho | Tempo de resposta rápido para listagens locais, utilizando paginação ou queries otimizadas. |
| **RNF04** | Persistência | Armazenamento relacional utilizando o banco de dados **SQLite** para facilidade de implantação local. |
| **RNF05** | Manutenibilidade | Arquitetura modular separada em camadas lógicas (Routes, Services, Repositories). |
| **RNF06** | Testabilidade | Alta cobertura de testes unitários e de integração utilizando o ecossistema **Pytest**. |
| **RNF07** | Portabilidade | Disponibilidade do ambiente de produção/desenvolvimento via **Docker Compose**. |

---

## 4. Regras de Negócio (RN)

As regras de negócio definem as restrições de comportamento e fluxos permitidos dentro do sistema.

> [!IMPORTANT]
> **RN01 — Vínculo Obrigatório de Pets**
> Todo pet registrado na base de dados deve estar obrigatoriamente associado a um tutor (cliente) válido existente no banco de dados.

> [!IMPORTANT]
> **RN02 — Vínculo Obrigatório de Atendimento**
> Qualquer registro de atendimento médico ou consulta deve estar estritamente associado a um pet cadastrado. Não é permitido criar atendimentos "órfãos".

> [!CAUTION]
> **RN03 — Controle de Acesso e Login**
> Todas as rotas de negócio (Clientes, Pets e Atendimentos) exigem autenticação do operador. Adicionalmente, apenas usuários com perfil de **Administrador** têm permissão para deletar registros (Clientes, Pets, Atendimentos ou Usuários).

> [!WARNING]
> **RN04 — Não Duplicidade de Chaves**
> O sistema não deve permitir o cadastro de clientes com o mesmo CPF ou E-mail. Do mesmo modo, cada operador (usuário) deve possuir um e-mail único para login.

---

## 5. Rastreabilidade no Código

Para guiar o desenvolvimento, os requisitos são mapeados diretamente na estrutura do backend:
- **RF01 - RF02**: Implementados em `app/routes/auth_routes.py`, `app/services/auth_service.py` e `app/core/security.py`.
- **RF03 - RF06**: Mapeados em `app/routes/cliente_routes.py` e validados pelo `app/services/cliente_service.py`.
- **RF07 - RF10**: Mapeados em `app/routes/pet_routes.py` e persistidos via `app/repositories/pet_repository.py`.
- **RF11 - RF12**: Mapeados em `app/routes/atendimento_routes.py`, aplicando a regra `RN02` no service correspondente.