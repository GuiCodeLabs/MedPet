# 🎤 Roteiro de Apresentação — MedPet

Este documento serve como um guia de apoio para a equipe durante a apresentação oficial do sistema **MedPet** para a disciplina de Análise e Projeto de Sistemas. Ele está organizado com marcações de tempo sugeridas e dicas práticas para a demonstração ao vivo.

---

## 1. Introdução e Abertura (⏱️ 1 a 2 min)

* **Objetivo**: Cumprimentar a banca, introduzir a equipe e expor o propósito geral do projeto.
* **Tópicos de Fala**:
  - Apresentar a equipe (Guilherme, Arllan, Pedro H., Pedro Antonio).
  - Explicar que o MedPet é uma aplicação web para gerenciamento básico de clínicas veterinárias criada para aplicar na prática conceitos de Engenharia de Software, modelagem UML e arquitetura de sistemas.

---

## 2. O Problema e a Proposta de Valor (⏱️ 2 min)

* **Objetivo**: Demonstrar o cenário e os problemas que o MedPet visa sanar.
* **Tópicos de Fala**:
  - Dificuldade enfrentada por clínicas de pequeno porte com fichas e prontuários manuais de papel ou planilhas desconexas.
  - Perda de histórico clínico de pets e registros redundantes de clientes tutor/CPF.
  - **A Proposta**: Um sistema rápido, leve e centralizado integrando cadastros, históricos de atendimentos médicos e controle de acesso seguro por operador.

---

## 3. Escopo e Limitações (⏱️ 1 min)

* **Objetivo**: Deixar claro o que faz parte do MVP da apresentação e o que foi deixado de fora do escopo.
* **Tópicos de Fala**:
  - **Incluso**: Sistema de autenticação JWT, CRUD de clientes e pets, e registro de atendimentos clínicos.
  - **Fora do escopo**: Módulos financeiros, integração de mensagens automatizadas com WhatsApp ou controle de estoque de farmácia.

---

## 4. Engenharia de Software e Modelagem (⏱️ 2 min)

* **Objetivo**: Apresentar os artefatos de análise e modelagem UML criados na fase de projeto.
* **Tópicos de Fala**:
  - **Casos de Uso**: Como dividimos as interações dos atores (Admin, Funcionário, Vet) com o sistema.
  - **Modelo de Dados (ERD)**: A estruturação física do banco SQLite, evidenciando as relações de tabelas (`clientes` -> `pets` -> `atendimentos`) e a regra de exclusão em cascata.
  - **Arquitetura (Componentes)**: Separação física clara entre frontend Streamlit e backend FastAPI.

---

## 5. Demonstração Prática do Sistema (⏱️ 4 min)

* **Objetivo**: Demonstrar o sistema real funcionando ao vivo.

> [!TIP]
> **Roteiro Recomendado para a Demo:**
> 1. **Login**: Realizar login com uma conta com perfil de Atendente e tentar excluir um pet para mostrar que o sistema bloqueia (Regra de Acesso).
> 2. **Cadastro**: Logar como Administrador, cadastrar um novo tutor (Cliente) e em seguida cadastrar um Pet associado a ele.
> 3. **Atendimento**: Logar com um perfil de Veterinário, selecionar o pet cadastrado e lançar uma nova consulta clínica/vacinação.
> 4. **Histórico**: Acessar o histórico clínico do pet para verificar se a consulta aparece em tempo real.
> 5. **Swagger**: Mostrar rapidamente a documentação interativa gerada automaticamente pelo FastAPI em `/docs` para evidenciar a robustez do backend.

---

## 6. Qualidade de Código e CI/CD (⏱️ 1 min)

* **Objetivo**: Evidenciar os padrões técnicos adotados para garantir a sustentabilidade do código.
* **Tópicos de Fala**:
  - **Testes Automatizados**: Uso do Pytest com banco de dados isolado em memória (`sqlite:///:memory:`).
  - **Pipeline de CI**: Integração contínua rodando Black (linter de formatação) e Pytest em cada Push ou Pull Request via GitHub Actions.

---

## 7. Conclusão e Encerramento (⏱️ 1 min)

* **Objetivo**: Finalizar a apresentação, destacar aprendizados e abrir espaço para perguntas da banca.
* **Tópicos de Fala**:
  - Aprendizado prático de desenvolvimento em camadas (MVC Adaptado + Repository + Services).
  - Agradecimento ao professor e colegas e abertura para perguntas.