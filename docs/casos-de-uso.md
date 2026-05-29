# 👥 Casos de Uso — MedPet

## 1. Visão Geral

Este documento apresenta os principais casos de uso do sistema **MedPet**, uma aplicação web voltada para a gestão básica de uma clínica veterinária.

Os casos de uso descrevem as interações entre os usuários e o sistema, mostrando quais funcionalidades estarão disponíveis e como elas serão utilizadas.

---

## 2. Atores do Sistema

### Administrador

Usuário com acesso completo ao sistema.

Responsabilidades:

- Gerenciar usuários
- Cadastrar clientes
- Cadastrar pets
- Registrar atendimentos
- Consultar informações
- Atualizar e excluir registros

### Funcionário

Usuário responsável pelas operações básicas do dia a dia da clínica.

Responsabilidades:

- Cadastrar clientes
- Cadastrar pets
- Consultar registros
- Registrar atendimentos

### Veterinário

Usuário responsável por consultar informações dos pets e registrar atendimentos.

Responsabilidades:

- Consultar dados de clientes e pets
- Registrar atendimentos veterinários
- Atualizar informações relacionadas ao atendimento

---

## 3. Lista de Casos de Uso

| Código | Caso de Uso | Ator Principal | Descrição |
|---|---|---|---|
| UC01 | Realizar login | Administrador, Funcionário, Veterinário | Permite que o usuário acesse o sistema com suas credenciais. |
| UC02 | Cadastrar usuário | Administrador | Permite cadastrar novos usuários no sistema. |
| UC03 | Cadastrar cliente | Administrador, Funcionário | Permite registrar os dados dos tutores dos pets. |
| UC04 | Consultar cliente | Administrador, Funcionário, Veterinário | Permite consultar clientes cadastrados. |
| UC05 | Atualizar cliente | Administrador, Funcionário | Permite editar os dados de um cliente. |
| UC06 | Excluir cliente | Administrador | Permite remover um cliente do sistema. |
| UC07 | Cadastrar pet | Administrador, Funcionário | Permite registrar os dados dos animais. |
| UC08 | Consultar pet | Administrador, Funcionário, Veterinário | Permite consultar informações dos pets cadastrados. |
| UC09 | Atualizar pet | Administrador, Funcionário, Veterinário | Permite editar dados dos pets. |
| UC10 | Excluir pet | Administrador | Permite remover um pet do sistema. |
| UC11 | Registrar atendimento | Administrador, Veterinário | Permite registrar consultas ou procedimentos realizados. |
| UC12 | Consultar atendimento | Administrador, Funcionário, Veterinário | Permite visualizar atendimentos registrados. |

---

## 4. Detalhamento dos Casos de Uso

## UC01 — Realizar Login

### Ator Principal

Administrador, Funcionário ou Veterinário.

### Objetivo

Permitir que o usuário acesse o sistema de forma segura.

### Pré-condições

- O usuário deve estar cadastrado no sistema.
- O usuário deve possuir e-mail e senha válidos.

### Fluxo Principal

1. O usuário acessa a tela de login.
2. O usuário informa e-mail e senha.
3. O sistema valida as credenciais.
4. O sistema libera o acesso às funcionalidades.
5. O usuário é direcionado para a tela principal.

### Fluxo Alternativo

- Caso os dados estejam incorretos, o sistema exibe uma mensagem de erro.

### Pós-condição

O usuário autenticado passa a ter acesso ao sistema.

---

## UC02 — Cadastrar Usuário

### Ator Principal

Administrador.

### Objetivo

Permitir que o administrador cadastre novos usuários no sistema.

### Pré-condições

- O administrador deve estar autenticado.

### Fluxo Principal

1. O administrador acessa a área de usuários.
2. O administrador seleciona a opção de novo cadastro.
3. O sistema exibe o formulário de cadastro.
4. O administrador informa os dados do usuário.
5. O sistema valida as informações.
6. O sistema salva o novo usuário.

### Fluxo Alternativo

- Caso algum campo obrigatório esteja vazio, o sistema solicita correção.
- Caso o e-mail já esteja cadastrado, o sistema informa duplicidade.

### Pós-condição

O novo usuário fica disponível para acesso ao sistema.

---

## UC03 — Cadastrar Cliente

### Ator Principal

Administrador ou Funcionário.

### Objetivo

Registrar os dados do tutor responsável pelo pet.

### Pré-condições

- O usuário deve estar autenticado.

### Fluxo Principal

1. O usuário acessa a área de clientes.
2. O usuário seleciona a opção de cadastrar cliente.
3. O sistema apresenta o formulário.
4. O usuário informa os dados do cliente.
5. O sistema valida os campos obrigatórios.
6. O sistema salva o cliente no banco de dados.

### Fluxo Alternativo

- Caso existam dados obrigatórios em branco, o sistema exibe uma mensagem de erro.

### Pós-condição

O cliente fica cadastrado no sistema.

---

## UC04 — Consultar Cliente

### Ator Principal

Administrador, Funcionário ou Veterinário.

### Objetivo

Permitir a busca e visualização dos clientes cadastrados.

### Pré-condições

- O usuário deve estar autenticado.
- Deve existir ao menos um cliente cadastrado.

### Fluxo Principal

1. O usuário acessa a área de clientes.
2. O sistema lista os clientes cadastrados.
3. O usuário pode visualizar os dados disponíveis.
4. O usuário pode utilizar filtros ou busca, caso disponível.

### Fluxo Alternativo

- Caso não existam clientes cadastrados, o sistema informa que nenhum registro foi encontrado.

### Pós-condição

Os dados do cliente são exibidos ao usuário.

---

## UC05 — Atualizar Cliente

### Ator Principal

Administrador ou Funcionário.

### Objetivo

Permitir a edição dos dados de um cliente cadastrado.

### Pré-condições

- O usuário deve estar autenticado.
- O cliente deve existir no sistema.

### Fluxo Principal

1. O usuário acessa a lista de clientes.
2. O usuário seleciona o cliente desejado.
3. O sistema exibe os dados cadastrados.
4. O usuário altera as informações necessárias.
5. O sistema valida os dados.
6. O sistema salva as alterações.

### Fluxo Alternativo

- Caso os dados sejam inválidos, o sistema solicita correção.

### Pós-condição

Os dados do cliente são atualizados.

---

## UC06 — Excluir Cliente

### Ator Principal

Administrador.

### Objetivo

Permitir a remoção de um cliente do sistema.

### Pré-condições

- O administrador deve estar autenticado.
- O cliente deve existir no sistema.

### Fluxo Principal

1. O administrador acessa a lista de clientes.
2. O administrador seleciona o cliente.
3. O sistema solicita confirmação da exclusão.
4. O administrador confirma a ação.
5. O sistema remove o cliente.

### Fluxo Alternativo

- Caso o administrador cancele a operação, nenhuma alteração é realizada.

### Pós-condição

O cliente é removido do sistema.

---

## UC07 — Cadastrar Pet

### Ator Principal

Administrador ou Funcionário.

### Objetivo

Registrar os dados de um pet vinculado a um cliente.

### Pré-condições

- O usuário deve estar autenticado.
- O cliente responsável pelo pet deve estar cadastrado.

### Fluxo Principal

1. O usuário acessa a área de pets.
2. O usuário seleciona a opção de cadastrar pet.
3. O sistema apresenta o formulário.
4. O usuário informa os dados do pet.
5. O usuário vincula o pet a um cliente.
6. O sistema valida as informações.
7. O sistema salva o pet.

### Fluxo Alternativo

- Caso nenhum cliente seja selecionado, o sistema solicita o vínculo com um tutor.

### Pós-condição

O pet fica cadastrado e vinculado ao cliente.

---

## UC08 — Consultar Pet

### Ator Principal

Administrador, Funcionário ou Veterinário.

### Objetivo

Permitir a visualização dos pets cadastrados.

### Pré-condições

- O usuário deve estar autenticado.
- Deve existir ao menos um pet cadastrado.

### Fluxo Principal

1. O usuário acessa a área de pets.
2. O sistema lista os pets cadastrados.
3. O usuário visualiza os dados do pet.
4. O usuário pode consultar o tutor vinculado ao pet.

### Fluxo Alternativo

- Caso não existam pets cadastrados, o sistema informa que nenhum registro foi encontrado.

### Pós-condição

Os dados do pet são exibidos ao usuário.

---

## UC09 — Atualizar Pet

### Ator Principal

Administrador, Funcionário ou Veterinário.

### Objetivo

Permitir a alteração dos dados de um pet cadastrado.

### Pré-condições

- O usuário deve estar autenticado.
- O pet deve existir no sistema.

### Fluxo Principal

1. O usuário acessa a lista de pets.
2. O usuário seleciona o pet desejado.
3. O sistema exibe os dados cadastrados.
4. O usuário altera as informações necessárias.
5. O sistema valida os dados.
6. O sistema salva as alterações.

### Fluxo Alternativo

- Caso os dados estejam inválidos, o sistema solicita correção.

### Pós-condição

Os dados do pet são atualizados.

---

## UC10 — Excluir Pet

### Ator Principal

Administrador.

### Objetivo

Permitir a remoção de um pet do sistema.

### Pré-condições

- O administrador deve estar autenticado.
- O pet deve existir no sistema.

### Fluxo Principal

1. O administrador acessa a lista de pets.
2. O administrador seleciona o pet.
3. O sistema solicita confirmação da exclusão.
4. O administrador confirma a ação.
5. O sistema remove o pet.

### Fluxo Alternativo

- Caso o administrador cancele a operação, nenhuma alteração é realizada.

### Pós-condição

O pet é removido do sistema.

---

## UC11 — Registrar Atendimento

### Ator Principal

Administrador ou Veterinário.

### Objetivo

Registrar informações sobre uma consulta ou procedimento veterinário.

### Pré-condições

- O usuário deve estar autenticado.
- O pet deve estar cadastrado.

### Fluxo Principal

1. O usuário acessa a área de atendimentos.
2. O usuário seleciona a opção de novo atendimento.
3. O sistema exibe o formulário de atendimento.
4. O usuário seleciona o pet.
5. O usuário informa a data, descrição, diagnóstico e observações.
6. O sistema valida os dados.
7. O sistema salva o atendimento.

### Fluxo Alternativo

- Caso o pet não esteja cadastrado, o sistema solicita o cadastro do pet antes do atendimento.

### Pós-condição

O atendimento fica registrado no sistema.

---

## UC12 — Consultar Atendimento

### Ator Principal

Administrador, Funcionário ou Veterinário.

### Objetivo

Permitir a visualização dos atendimentos registrados.

### Pré-condições

- O usuário deve estar autenticado.
- Deve existir ao menos um atendimento registrado.

### Fluxo Principal

1. O usuário acessa a área de atendimentos.
2. O sistema lista os atendimentos registrados.
3. O usuário visualiza as informações do atendimento.
4. O usuário pode consultar o pet relacionado ao atendimento.

### Fluxo Alternativo

- Caso não existam atendimentos cadastrados, o sistema informa que nenhum atendimento foi encontrado.

### Pós-condição

Os dados do atendimento são exibidos ao usuário.

---

## 5. Regras Relacionadas aos Casos de Uso

| Código | Regra | Descrição |
|---|---|---|
| RN01 | Login obrigatório | Apenas usuários autenticados podem acessar o sistema. |
| RN02 | Cliente obrigatório | Todo pet deve estar vinculado a um cliente. |
| RN03 | Pet obrigatório | Todo atendimento deve estar vinculado a um pet. |
| RN04 | Permissão de exclusão | Apenas administradores podem excluir registros importantes. |
| RN05 | Dados obrigatórios | Cadastros devem possuir campos mínimos preenchidos. |

---

## 6. Considerações Finais

Os casos de uso apresentados representam as principais funcionalidades do sistema **MedPet**.

Eles servem como base para:

- A criação dos diagramas UML
- O desenvolvimento das funcionalidades
- A divisão de tarefas entre os integrantes
- A validação dos requisitos do sistema
- A apresentação final do projeto

Este documento poderá ser atualizado conforme o sistema evoluir durante o desenvolvimento.