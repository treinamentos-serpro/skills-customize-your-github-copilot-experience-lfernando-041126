# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Crie uma API REST para cadastrar e gerenciar livros usando o framework FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Iniciar a API e listar livros

#### Descrição
Complete o starter code para iniciar a aplicação e disponibilizar uma rota que liste os livros armazenados.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn com `pip install fastapi uvicorn`.
- Executar a aplicação com `uvicorn starter-code:app --reload`.
- Implementar `GET /books`, retornando a lista de livros (vazia quando não houver livros).
- Permitir testar a rota pela documentação interativa em `/docs`.

### 🛠️ Criar e consultar livros

#### Descrição
Adicione rotas para cadastrar um livro e consultar um livro específico pelo seu identificador.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para receber título e autor e atribuir um identificador único.
- Retornar o livro criado com o código de status HTTP `201`.
- Implementar `GET /books/{book_id}` para retornar o livro solicitado.
- Retornar o código de status HTTP `404` quando o identificador não existir.

### 🛠️ Atualizar e excluir livros

#### Descrição
Complete as operações de gerenciamento para atualizar ou remover um livro existente.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar o título e o autor do livro.
- Implementar `DELETE /books/{book_id}` e responder com o código HTTP `204` quando a exclusão for concluída.
- Retornar o código de status HTTP `404` para atualizações ou exclusões de identificadores inexistentes.
- Confirmar, usando `/docs`, que as rotas de criação, consulta, atualização e exclusão funcionam.