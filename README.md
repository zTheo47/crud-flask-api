# 🚀 Flask CRUD API - Sistema de Usuários

Este projeto é uma API REST desenvolvida com Flask e SQLite, com o objetivo de praticar conceitos de backend e operações CRUD.

---

## 📌 Sobre o projeto

A API permite gerenciar usuários através de operações básicas:

- Criar usuários
- Listar usuários
- Atualizar usuários
- Deletar usuários

O foco do projeto é aprendizado de desenvolvimento de APIs e estruturação de backend com Python.

---

## ⚙️ Tecnologias utilizadas

- Python
- Flask
- SQLite
- JSON (API REST)

---

## 📁 Estrutura do projeto

crud-flask-api/
- app.py → código principal da API
- README.md → documentação do projeto

---

## 🌐 Endpoints da API

### 📥 Listar usuários
GET /usuarios  
Retorna todos os usuários cadastrados.

---

### ➕ Criar usuário
POST /usuarios  
Cria um novo usuário.

Exemplo de corpo da requisição:
{
  "nome": "João",
  "idade": 15
}

---

### ✏️ Atualizar usuário
PUT /usuarios/<id>  
Atualiza os dados de um usuário existente.

Exemplo de corpo da requisição:
{
  "nome": "Pedro",
  "idade": 16
}

---

### ❌ Deletar usuário
DELETE /usuarios/<id>  
Remove um usuário pelo ID.

---

## ▶️ Como executar o projeto

Instale as dependências:

pip install flask

Execute a aplicação:

python app.py

Acesse no navegador:

http://127.0.0.1:5000

---

## 🧪 Como testar

Você pode testar a API usando:

- Postman
- Insomnia
- curl
- fetch no JavaScript

---

## 🎯 Objetivo do projeto

Este projeto foi criado para praticar:

- Desenvolvimento de APIs REST com Flask
- Operações CRUD
- Estrutura de backend
- Manipulação de dados com SQLite

---

## 👨‍💻 Autor

Desenvolvido por Stanley Alves
