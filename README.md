<h1 align="center"> Sistema de um banco digital  - Fipay</h1>

<h4 align="center">   
Deveríamos criar uma carteira digital de um banco onde o usuário poderia fazer compras, depósitos e transferências. Além disso, o app possibilitaria fazer simulações de rendimento do CDI e, além disso, foram consumidos dados da API fonecida pela <a href="https://hgbrasil.com/status/finance">HG finance</a> a qual possui informações de conversões da moeda BRL para outras 9 (nove) moedas, valores de mercado como IBOVESPA, DOW JONES, valores de bitcoin e também dados de taxa como CDI diárioe e SELIC. Deveria ser criado também um banco de dados onde as informações de cadastro, notificações de transferências e movimentações do dinheiro seriam armazenadas.
</h4>

## Tópicos 
- [Imagens do REST API](#imagens-do-rest-api) 
- [Informações da API](#informações-da-hg-finance-api-)
- [APPs django criados](#apps-django-criados)
- [Passo a passo da implementação](#passo-a-passo-da-implementação-)
- [Instalações](#instalações-)

# Imagens do REST API 
<h4 align='center'>API já em deploy <a href='https://squad1-banco.herokuapp.com/'>aqui</a>.

![image](https://user-images.githubusercontent.com/94690905/153208478-1543746b-700d-4351-b811-53195334cd46.png)</h4>


<h4 align='center'>API já em deploy <a href='https://squad1-banco.herokuapp.com/financeiro/'>aqui</a>. Endpoint: /financeiro mostra informações consumidas da HG Finance
  
  ![image](https://user-images.githubusercontent.com/94690905/153211976-c02963e7-ce0d-42c1-896c-66499664803b.png)</h4>


# Informações da HG Finance API 📜
- moeda (conversões da moeda base BRL)
- mercado (informações de IBOVESPA, IFIX, etc)
- bitcoin (informações de Blockchain, foxbit, etc)
- taxas (taxas diárias de SELIC, CDI, etc)

# APPs django criados
  - Cliente (possui formas de cadastros e listagem de clientes do sistema)
  - Compra (informa pelo CPF qual cliente está fazendo uma compra e lista as compras realizadas)
  - Depósito (através do CPF informa qual cliente está recebendo um depósito)
  - Financeiro (consumo da HG Finance API e cálculo do rendimento com CDI
  - Notificação (mostra histórico de transferências entre clientes)
  - Transferência (realiza transferência entre clientes através de seus respectivos CPF)

# Passo a passo da implementação 🏃
- ### Acessar a HG Brasil
    <h5>Acessando as informações da HG Brasil e consumindo apenas os dados necessários</h5>
- ### Criar Projeto Django
    <h5>Criar um projeto Django, criar os APPs, fazer as configurações, instalar pacotes e ambiente virtual</h5>
- ### Fazer deploy em domínio gratuito
    <h5>Deve-se instalar o <a href='https://devcenter.heroku.com/articles/heroku-cli'>Heroku CLI</a> e abrir o bash onde está os arquivos e fazer o login com sua conta heroku e criar um projeto</h5>
    
    ```
    heroku login
    heroku create <nome do dominio>
    ```
    <h5>Fazer os commits para o deploy</h5>   
    
    ```
    git add .
    git commit -m "deploy"
    heroku addons:create heroku-postgresql:hobby-dev
    git push heroku master
    ```
    <h5>Fazer migrações do banco de dados</h5>   
    
    ```
    heroku run python manage.py migrate
    ```
    
- ### Implementar Django REST Framework
    <h5>Utilizar padrão REST para e conseguir acessar os dados em JSON pelo navegador</h5>
    <h5>Criar apps:</h5>
    
    ```
    django-admin startapp cliente
    ```
    
    <h5>Após criar os Apps, fazer as importações de tabela para o banco padrão do Django (SQlite3)</h5>
    
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
    
    <h5>Iniciar localmente o servidor</h5>
    
    ```
    python manage.py runserver
    ```

# Instalações 🔧

- 1º: instalar o Django:
```
pip install django 
```
- 2º: instalar o REST framework:
```
pip install djangorestframework 
```
- 3º: instalar o Requests:
```
pip install requests 
```
- 4º: instalar o gunicorn:
```
pip install gunicorn 
```
- 5º: instalar o Django-heroku:
```
pip install django-heroku 
```
- OPCIONAL: instalar bibliotecas do 'requirements.txt':
```
pip install requirements.txt
```
