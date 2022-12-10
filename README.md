<h1 align="center">API Autenticação</h1>

<p align="center">API para autenticação de usuários</p>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![fast-api](https://img.shields.io/badge/framework-FastAPI-blue)
![database](https://img.shields.io/badge/DB-MySQL-blue)
[![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/Naereen/StrapDown.js)

Indice
=================
 * [Sobre](#-sobre)
 * [Tecnologias Utilizadas](#-tecnologias-utilizadas)
 * [Pré-requisitos](#-pré-requisitos)
 * [Como Executar o Projeto](#-como-executar-o-projeto)
 * [Autor](#-autor)

## 🔖&nbsp; Sobre

O projeto **API Autenticação** é uma API feita em Python onde o usuário pode realizar um cadastro, que será salvo no banco de dados, e com esse cadastro também poderá fazer login no sistema. O sistema conta com utilização de token para validar o acesso do usuário ao sistema. Esse projeto foi criado dentro do curso **Python Full** com o intuito de colocarmos em prática o conteúdo estudado durante o módulo de API com a biblioteca FastAPI.

---

## 🚀 Tecnologias utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PyMySQL](https://pypi.org/project/PyMySQL/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [MySQL](https://www.mysql.com/)
- [Wampserver](https://www.wampserver.com/en/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 🗂 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/downloads/), [FastAPI](https://fastapi.tiangolo.com/), [MySQL](https://www.mysql.com/), [PyMSQL](https://pypi.org/project/PyMySQL/), [SQLAlchemy](https://www.sqlalchemy.org/), [Wampserver](https://www.wampserver.com/en/), [Uvicorn](https://www.uvicorn.org/). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/) e um sistema de gerenciamento de banco de dados como o phpMyAdmin que pode ser obtido junto ao Wampserver. 

## 🎲 Como executar o projeto

```bash
# Clone este repositório
git clone <https://github.com/CirNNe/chat-tempo-real.git>
# Execute o Wampserver
# Abra o phpMyAdmin ou outro SGBD de sua preferência, lá você poderá visualizar as alterações no banco de dados (por padrão a porta será 3306)
http://localhost:3306/phpmyadmin/
# Crie o banco de dados com o nome 'apiautenticacaomysql' ou troque o nome no código (arquivo model.py, linha 10) e crie o banco de dados com o nome desejado
# Na pasta do projeto, em seu terminal, execute o servidor Uvicorn para rodar a API
uvicorn main:app --reload
# Abra o FastAPI docs no seu navegador, lá será o local para manusear a API
http://127.0.0.1:3306/docs
```

## 👨‍💻 Autor

<a href="https://github.com/CirNNe">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/98779843?s=400&u=0acf3d526d374b620501ea180d5c81c3ff998c42&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Higor Cirne</b></sub></a> <a href="https://github.com/CirNNe" title="GitHub"></a>

👋🏽 Entre em contato!

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/higorcirne/)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/higordev_/)
