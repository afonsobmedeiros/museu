# Projeto Museu.

## Para executar o projeto

Dependencias:
 - Poetry
 - bottle
 - pymysql
 - pyjwt
 - passlib

Com poetry instalado realizar instalação das demais depêndencias.

```sh
poetry install --no-root
```

Criar arquivo de configuração: my.cnf:

```cnf
[client]
host=SEU_HOST
user=SEU_USUARIO
password=SUA_SENHA
database=SEU_BANCO
```

Criar tabelas com o arquivo `SCRIPTS_DATABASE/CREATE_TABLES.sq`.

Insira um novo usuário, tente utilizar o prompt iterativo para poder usar o método gen_hash.

Depois disso é só executar:

```sh
python application.py
```