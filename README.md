<h1 align='center'><em>FastAPI Zero(Async)</em> em: Listas To-do's :zap::spiral_notepad:</h1>

<div align='center'>
<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-005571?logo=fastapi">
<img alt="Postgres" src="https://img.shields.io/badge/postgres-%23316192.svg?logo=postgresql&logoColor=white">
<img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white">
<img alt="Creative Commons License" src="https://img.shields.io/badge/License-Creative%20Commons-white">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/amanmdest/fast_zero_sync?color=orange">
</div>
<br>
<p align='center'>>>> <q>O simples bem feito!</q> <<<</p>
<p align='center'>API desenvolvida no curso <a href="https://fastapidozero.dunossauro.com/">FastAPI do Zero</a> do mestrão @Dunossauro, presença importante na comunidade python.</p>

## Projetos Relacionados
#### [Fast Zero](https://github.com/amanmdest/fast_zero_sync) - Versão síncrona do projeto.
#### [MADR(Meu Acervo Digital de Romances)](https://github.com/amanmdest/madr_novels) - Projeto Final de Conclusão do Curso
## Sobre a FastAPI-Zero
- Nessa API lidamos com o cadastro, autenticação e autorizações de usuários que podem criar, editar e deletar suas respectivas notas que possuem 5 estados de tarefas: 'draft'= rascunho, 'todo'= para fazer, 'doing'= fazendo, 'done'= feito, 'trash'= descarte
## Pontos de Destaque
- Agora totalmente assíncrono, o projeto conta com os recursos do FastAPI e do SQLAlchemy para operações mais eficientes e escaláveis.
- TDD e cobertura da API com testes determinísticos.
- Schemas, manipulação de modelos de dados com Pydantic e SQLAlchemy.
- Migrações de banco de dados com alembic.
- Autenticação e autorização com JWT.
- Introdução de conceitos e boas práticas como 12 fatores e variáveis de ambiente.
- Containerização com docker e docker-compose, e criação de uma imagem PostgreSQL.
- Pipeline/Workflow automatizado de Integração Contínua(CI) com GitHub Actions.
- Deploy pela plataforma Fly.io.
## Bibliotecas | Ferramentas
- [Python 3.12](https://www.python.org/downloads/release/python-3120/) -> Última versão Python testada.
- [FastAPI](https://fastapi.tiangolo.com/) -> Web Framework de alto desempenho para construir API's com Python.
- [uvicorn](https://www.uvicorn.org/) -> Servidor ASGI.
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) -> Biblioteca open-source com Toolkit de SQL e Object Relational Mapper(ORM).
- [Pydantic](https://github.com/pydantic/pydantic/releases/tag/v2.9.2) -> Validação de dados e alguns gerenciamentos de configuração.
- [alembic](https://alembic.sqlalchemy.org/en/latest/) -> Ferramenta de migração de banco de dados.
### 🛠️ Dependências Desenvolvimento:
- [poetry](https://python-poetry.org/docs/#zsh) -> Gerenciador de pacotes do Python (usado para configurar o ambiente).
- [taskipy](https://pypi.org/project/taskipy/) -> Executor de tarefas para projetos python.
- [ruff](https://docs.astral.sh/ruff/) -> Formatador e Linter Python extremamente rápido, escrito em Rust.
- [ignr](https://pypi.org/project/ignr/) -> Plugin para gerar um arquivo .gitignore baseado na linguagem que voce definir.
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/) -> Autenticador entre duas partes, por meio de um token assinado que segue o padrão(RFC-7519)
- [pwdlib](https://pypi.org/project/pwdlib/) -> auxiliar moderno p/ hashing de passwords
- [psycopg-binary](https://pypi.org/project/psycopg-binary/)  -> Adaptador de PostgreSQL para Python.
### 🧪 Dependências Testes:
- [pytest](https://docs.pytest.org/en/stable/index.html) -> Testes simples e poderosos com Python.
- [pytest-asyncio](https://pypi.org/project/pytest-asyncio/) -> Plugin do pytest que fornece suporte para corrotinas como funçõoes de teste.
- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) -> Um plugin para produzir relatórios de cobertura de testes.
- [factory-boy](https://factoryboy.readthedocs.io/en/latest/) -> Uma biblioteca que permite criar objetos de modelo de teste de forma rápida e fácil.
- [freezegun](https://github.com/spulec/freezegun) -> Uma biblioteca que permite "congelar" o tempo em um ponto específico ou avançá-lo conforme necessário durante os testes.
- [testcontainers](https://github.com/testcontainers) -> Facilita o uso de contêineres Docker para testes funcionais e de integração.
## Rode localmente
1. Clone o repositório:
```bash
  git clone https://github.com/amanmdest/fastapi_zero.git
```
2. Instale dependências:
```bash
  poetry install
```
3. Para rodar o projeto junto ao banco de dados postgres é necessário criar um arquivo .env na raiz do projeto como o do exemplo abaixo:
```bash
  .env
  DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db"
  SECRET_KEY="8bf15dc4b43e98a24f62891ebf090e6839d99bce6c669de759706a243ef73737" # exemplo token_hex
  ALGORITHM="HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES=30
  
  POSTGRES_USER=app_user
  POSTGRES_DB=app_db
  POSTGRES_PASSWORD=app_password
```
4. Buildar a imagem e criar/iniciar o conteiner da aplicação junto ao banco de dados (necessário instalar [docker-compose](https://docs.docker.com/compose/install/)):
```bash
  docker compose up --build
```
Ou para rodar o projeto de forma limitada no servidor local Uvicorn sem banco de dados:
```bash
  task run
```
e acesse: http://127.0.0.1:8000/docs

## Imagens
<div align="center">
  <img src="https://github.com/amanmdest/fastapi_zero/blob/main/images/fastapi_zero_DER.png" alt="fastapi_zero_DER" />
  <p>Diagrama Entidade-Relacionamento</p>
  
  <img src="https://github.com/amanmdest/fastapi_zero/blob/main/images/fastapi_zero_coverage.png" alt="fastapi_zero_coverage" />
  <p>HTML Coverage - Cobertura de testes do projeto</p>
  
  <img src="https://github.com/amanmdest/fastapi_zero/blob/main/images/fastapi_zero_endpoints.png" alt="fastapi_zero_endpoints" />
  <p>Documentação Swagger - Endpoints Rotas da Api</p>
</div>
