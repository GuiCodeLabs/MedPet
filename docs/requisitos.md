# 📋 Requisitos do Sistema — MedPet

## 1. Visão Geral

O **MedPet** é um sistema web voltado para a gestão básica de uma clínica veterinária.

O objetivo do sistema é permitir o cadastro, consulta, atualização e exclusão de informações relacionadas a usuários, clientes, pets e atendimentos veterinários.

Este documento apresenta os requisitos funcionais e não funcionais do sistema, servindo como base para o desenvolvimento, modelagem UML e apresentação do projeto.

---

## 2. Objetivo dos Requisitos

Os requisitos têm como finalidade definir o que o sistema deve fazer e quais características de qualidade ele deve possuir.

A partir deles, será possível orientar:

- O desenvolvimento do backend
- A criação da interface web
- A modelagem dos casos de uso
- A estruturação do banco de dados
- A criação dos testes do sistema

---

## 3. Requisitos Funcionais

Os requisitos funcionais representam as funcionalidades que o sistema deve oferecer aos usuários.

| Código | Requisito | Descrição |
|---|---|---|
| RF01 | Cadastrar usuário | O sistema deve permitir o cadastro de usuários que terão acesso à aplicação. |
| RF02 | Autenticar usuário | O sistema deve permitir que o usuário realize login com suas credenciais. |
| RF03 | Cadastrar cliente | O sistema deve permitir o cadastro dos tutores dos pets. |
| RF04 | Consultar clientes | O sistema deve permitir a listagem e consulta dos clientes cadastrados. |
| RF05 | Atualizar cliente | O sistema deve permitir a edição dos dados de um cliente cadastrado. |
| RF06 | Excluir cliente | O sistema deve permitir a remoção de clientes do sistema. |
| RF07 | Cadastrar pet | O sistema deve permitir o cadastro dos pets vinculados aos clientes. |
| RF08 | Consultar pets | O sistema deve permitir a visualização dos pets cadastrados. |
| RF09 | Atualizar pet | O sistema deve permitir a alteração dos dados de um pet. |
| RF10 | Excluir pet | O sistema deve permitir a exclusão de pets cadastrados. |
| RF11 | Registrar atendimento | O sistema deve permitir o registro de atendimentos veterinários. |
| RF12 | Consultar atendimentos | O sistema deve permitir a consulta dos atendimentos registrados. |

---

## 4. Requisitos Não Funcionais

Os requisitos não funcionais representam características de qualidade, segurança, desempenho e organização do sistema.

| Código | Requisito | Descrição |
|---|---|---|
| RNF01 | Segurança | O sistema deve possuir controle de acesso por autenticação. |
| RNF02 | Usabilidade | A interface deve ser simples, intuitiva e fácil de utilizar. |
| RNF03 | Performance | O sistema deve responder às principais operações em tempo aceitável. |
| RNF04 | Organização | O código deve seguir uma estrutura modular e organizada. |
| RNF05 | Manutenibilidade | O sistema deve permitir futuras alterações e melhorias com facilidade. |
| RNF06 | Persistência | Os dados devem ser armazenados em banco de dados relacional. |
| RNF07 | Documentação | O sistema deve possuir documentação básica das funcionalidades e estrutura. |
| RNF08 | Testabilidade | O sistema deve permitir a criação de testes para validar suas funcionalidades. |

---

## 5. Regras de Negócio

| Código | Regra | Descrição |
|---|---|---|
| RN01 | Cliente obrigatório para pet | Todo pet cadastrado deve estar vinculado a um cliente. |
| RN02 | Login obrigatório | Apenas usuários autenticados devem acessar as funcionalidades principais. |
| RN03 | Dados obrigatórios | Cadastros devem conter os campos mínimos necessários. |
| RN04 | Atendimento vinculado a pet | Todo atendimento deve estar associado a um pet cadastrado. |
| RN05 | Não duplicidade | O sistema deve evitar cadastros duplicados quando possível. |

---

## 6. Entidades Principais

As principais entidades previstas para o sistema são:

### Usuário

Representa quem acessa o sistema.

Campos sugeridos:

- ID
- Nome
- E-mail
- Senha
- Tipo de usuário

### Cliente

Representa o tutor responsável pelo pet.

Campos sugeridos:

- ID
- Nome
- CPF
- Telefone
- Endereço

### Pet

Representa o animal cadastrado na clínica.

Campos sugeridos:

- ID
- Nome
- Espécie
- Raça
- Idade
- ID do cliente

### Atendimento

Representa o registro de uma consulta ou procedimento.

Campos sugeridos:

- ID
- Data
- Descrição
- Diagnóstico
- Observações
- ID do pet

---

## 7. Prioridade dos Requisitos

### Alta Prioridade

- Cadastro de usuários
- Login
- Cadastro de clientes
- Cadastro de pets
- Registro de atendimentos
- Consulta de dados

### Média Prioridade

- Atualização de registros
- Exclusão de registros
- Organização dos dados em tabelas
- Validação de campos

### Baixa Prioridade

- Relatórios simples
- Melhorias visuais
- Filtros avançados
- Controle de permissões mais detalhado

---

## 8. Considerações Finais

Este documento define os requisitos iniciais do sistema **MedPet**.

Ele será utilizado como base para o desenvolvimento do projeto, criação dos casos de uso, modelagem UML e apresentação final da disciplina de Análise e Projeto de Sistemas.

O sistema foi pensado para atender ao escopo inicial do projeto, mantendo uma estrutura simples, funcional e organizada.