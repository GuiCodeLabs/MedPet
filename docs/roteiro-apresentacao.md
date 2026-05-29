# 🎤 Roteiro da Apresentação — MedPet

## 1. Introdução

Olá, professor e colegas.

Nós somos o grupo responsável pelo desenvolvimento do **MedPet**, um sistema web voltado para a gestão básica de uma clínica veterinária.

O projeto foi desenvolvido para a disciplina de **Análise e Projeto de Sistemas**, com o objetivo de aplicar conceitos de Engenharia de Software, levantamento de requisitos, casos de uso, arquitetura de software e desenvolvimento de uma aplicação web completa.

---

## 2. Apresentação da Equipe

A equipe é formada por:

- Guilherme
- Arllan
- Pedro H.
- Pedro Antonio

A divisão do trabalho foi pensada para que todos pudessem participar ativamente tanto do planejamento e documentação quanto da implementação do Backend e Frontend.

---

## 3. Tema do Projeto

O tema escolhido pelo grupo foi o gerenciamento de uma **clínica veterinária**.

O sistema recebeu o nome de **MedPet** e tem como proposta auxiliar no controle de informações essenciais da clínica, substituindo processos manuais e planilhas por uma plataforma digital centralizada.

---

## 4. Problema Identificado

Muitas clínicas veterinárias de pequeno porte ainda registram suas informações de forma manual, o que gera diversos problemas, como:

- Dificuldade para encontrar o histórico clínico dos animais;
- Perda de dados importantes;
- Desorganização no agendamento e controle de atendimentos;
- Possibilidade de registros duplicados de clientes e pets.

Diante disso, o MedPet surge como uma solução web simples e direta para resolver esses gargalos.

---

## 5. Objetivo do Sistema

O objetivo principal do MedPet é facilitar a gestão do dia a dia da clínica veterinária.

Com o sistema, é possível:

- Gerenciar os perfis de usuários do sistema;
- Cadastrar e consultar clientes (tutores);
- Cadastrar os pets, vinculando-os aos seus tutores;
- Registrar e consultar o histórico de atendimentos veterinários.

---

## 6. Público-Alvo

O sistema foi desenhado para atender clínicas de pequeno e médio porte.

Os principais usuários incluem:

- **Administradores:** Que possuem controle total sobre o sistema;
- **Atendentes/Recepção:** Que realizam o cadastro de clientes e pets;
- **Veterinários:** Que consultam as informações clínicas e registram os atendimentos.

---

## 7. Escopo do Sistema

Focamos em entregar um MVP (Minimum Viable Product) funcional e condizente com os prazos acadêmicos da disciplina.

### O sistema inclui:
- Cadastro e Autenticação de usuários (Login com JWT);
- Operações de CRUD (Criar, Ler, Atualizar e Excluir) para Clientes e Pets;
- Registro de Atendimentos;
- Interface visual intuitiva.

### O sistema NÃO inclui neste momento:
- Aplicativo mobile para tutores;
- Módulo financeiro e emissão de notas fiscais;
- Integração com WhatsApp ou envio de notificações automáticas.

---

## 8. Arquitetura e Padrões de Projeto

Para garantir um código limpo e manutenível, adotamos uma arquitetura dividida em três camadas principais:

- **Frontend:** Interface de comunicação com o usuário.
- **Backend:** API RESTful que processa as regras de negócio.
- **Banco de Dados:** Camada de persistência.

No backend, aplicamos uma variação do padrão MVC voltada para APIs, utilizando os padrões **Repository** (para isolar o banco de dados) e **Service Layer** (para separar as regras de negócio das rotas HTTP).

---

## 9. Tecnologias Utilizadas

Escolhemos uma stack moderna e unificada em Python:

- **Python** como linguagem principal.
- **FastAPI** para a construção rápida e robusta da API REST no backend.
- **Streamlit** para o frontend, permitindo criar interfaces web ricas de forma ágil.
- **SQLite** como banco de dados relacional (ideal pela simplicidade acadêmica).
- **SQLAlchemy** como nosso ORM (Object-Relational Mapping).
- **Pydantic** para validação estrita de dados na API.
- **Pytest** para garantir a qualidade do sistema por meio de testes automatizados.
- **Git/GitHub** para versionamento de código e colaboração.

---

## 10. Estrutura das Entidades

O banco de dados e a arquitetura do projeto foram modelados em torno de quatro entidades principais e padronizadas:

1. **Usuario:** Representa quem acessa e opera o sistema.
2. **Cliente:** Representa o tutor financeiro e responsável.
3. **Pet:** O animal de estimação obrigatoriamente vinculado ao cliente.
4. **Atendimento:** O registro clínico vinculado ao pet.

Essa nomenclatura (usuario, cliente, pet, atendimento) foi utilizada rigorosamente em todo o código, desde os modelos de banco de dados até os endpoints da API.

---

## 11. Divisão da Equipe

A responsabilidade pelo desenvolvimento e documentação foi dividida da seguinte forma:

- **Guilherme:** Desenvolvimento do backend base, estruturação do banco de dados e fluxos de autenticação.
- **Arllan:** Criação dos módulos e rotas de Clientes e Pets, além da elaboração dos diagramas UML.
- **Pedro H.:** Estruturação do frontend no Streamlit e integração total da interface com a API.
- **Pedro Antonio:** Desenvolvimento dos módulos de atendimentos/prontuários, criação dos testes automatizados e refinamento da documentação.

---

## 12. Resultados e Conclusão

Ao longo da disciplina, conseguimos evoluir desde o levantamento dos requisitos até a implementação de um sistema web modular e funcional. 

O MedPet atende a um problema real de forma prática, demonstrando a integração bem-sucedida entre uma interface visual desenvolvida em Streamlit e uma API rápida e segura feita em FastAPI. 

Acreditamos que o projeto apresenta uma arquitetura sólida, pronta para receber novas funcionalidades no futuro — como controle de vacinas e módulos financeiros — validando todos os conhecimentos práticos e teóricos adquiridos em Análise e Projeto de Sistemas.

---

## 13. Encerramento

Esse foi o nosso projeto **MedPet**.

Agradecemos a atenção de todos e estamos à disposição para eventuais dúvidas!