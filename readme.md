# Teste de Desenvolvimento Django - IGS Employee Manager
Este é um projeto desenvolvido em Django como teste técnico para a empresa IGS. O objetivo do projeto é criar uma API e um site para gerenciar funcionários e departamentos de uma empresa.

## Como usar
Para utilizar o IGS Employee Manager, é necessário ter o Python 3.8 ou superior e o Django 3.2 ou superior instalados em sua máquina.

Para instalar as dependências do projeto, execute o seguinte comando:
```bash
pip install -r requirements.txt
```

Para criar as tabelas do banco de dados, execute o seguinte comando:
```bash
python manage.py migrate
```

Para rodar o projeto, execute o seguinte comando:
```bash
python manage.py runserver
```

Isso iniciará o servidor de desenvolvimento em http://127.0.0.1:8000/. A partir daí, você pode acessar a página web do projeto e utilizar a API

## Acesso ao painel administrativo
Acesse a rota http://127.0.0.1:8000/admin/ com o usuário admin e a senha 123 para acessar o painel administrativo do projeto.

## API
A API do projeto é composta por duas rotas para gerenciar departamentos e funcionários.

## Listagem de departamentos
Para listar todos os departamentos cadastrados, utilize o método GET em http://127.0.0.1:8000/api/departments/.

## Criação de departamentos
Para criar um novo departamento, utilize o método POST em http://127.0.0.1:8000/api/departments/ com o seguinte corpo:
```json
{
    "name": "Nome do departamento"
}
```

## Deleção de departamento
Para deletar um departamento existente, utilize o método DELETE em http://127.0.0.1:8000/api/departments/:id/, onde :id é o ID do departamento a ser deletado.

## Listagem de funcionários
Para listar todos os funcionários cadastrados, utilize o método GET em http://127.0.0.1:8000/api/employees/.

## Criação de funcionários
Para criar um novo funcionário, utilize o método POST em http://127.0.0.1:8000/api/employees/ com o seguinte corpo:
```json
{
    "name": "Nome do funcionário",
    "email": "Email do funcionário",
    "department": "ID do departamento"
}
```

## Deleção de funcionário
Para deletar um funcionário existente, utilize o método DELETE em http://127.0.0.1:8000/api/employees/:id/, onde :id é o ID do funcionário a ser deletado.

## Site
O site do projeto é composto por duas páginas para gerenciar funcionários e departamentos.

# Listar e Remover funcionários
A página inicial do site em http://127.0.0.1:8000/ lista todos os funcionários cadastrados e permite a deleção de funcionários individuais.

# Adicionar funcionários
A página http://127.0.0.1:8000/employee-form/ permite a criação de novos funcionários, solicitando o nome do funcionário e o ID do departamento ao qual o funcionário pertence.

## Listar, criar e remover departamentos
A página http://127.0.0.1:8000/department/ lista todos os departamentos cadastrados e permite a criação de novos departamentos e a deleção de departamentos individuais.
