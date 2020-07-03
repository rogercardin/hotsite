Passo a Passo para rodar a aplicacao
-Instala��o do Pyhton e as vari�veis de ambiente no windows
-Usando o Django que � um Framework baseado na linguagem Python
-Framework r�pido e escal�vel, excelente performace.
-Baseado em arquitetura MTV
-Models(Classes e Objetos e camada de acesso aos dados ao BD)
-View(Controllers do MTV, comunica��o entre o template e o Model)
-URL'S(Define as rotas ou seja para onde ir� suas requisi��es e respostas(request e response)
-Templates(Equivalente as views e arquivos est�ticos)
-Baseados em aplica�oes(pode reusar as suas aplica��es)
-Adminitra��o com um Painel Admnistrativo com solu��es r�pidas (Django Admin)
-Instala��o no windows
Dentro do terminal do python:
Abra a interface IDLE(Python GUI)
Digite django-admin startproject hotsite
A estrutura do projeto hotsite:
diretorios: hotsite,combate,manage
-No sub-diret�rio hotsite: Defini��o da estrutura com arquivos em .py(settings,admin,urls,wsgi)
-settings: configura�oes: STATIC_URL:'/static/' 
ROOT_URLCONF:'hotsite.urls'
INSTALLED_APPS:'combate'
DATABASES:Definisdas dentro do servidor local wampp64
'ENGINE': 'django.db.backends.mysql'
'NAME': 'combate'
'USER': 'root'
'PASSWORD': '',
    
-No sub-diret�rio combate: Defini��o de arquivos est�ticos, templates, admin,forms, models,urls.
Models: Modelo do BD(Com a Classe Post, tamb�m s�o definidas as tabelas que ser�o criadas dinamicamente)
URLS's (defini��o das URLS's do sistema como: lista-todos,novo)
VIEWS(S�o os controles da aplica��o, definidos como lista,novo,atualizar e deletar(CRUD)
Templates(localizados os arquivos em html com css e javascript e utiliza��o do BootstrapCDN)

Execu��o:

1-Digite o cmd no Windows e na pasta hotsite digite: cd hotsite e dentro dele o comando do python manage.py validate
e depois manage.py runserver para conectar o servidor.
2- Na Barra de endere�os: digite a seguinte URL:http://127.0.0.1:8000/admin/ para entrar no Painel Administrativo do Django
3- Para fazer login na aplica��o digite login: admin e password: 123456
4- O sistema apresentar� a tela de Combate administration com os Posts j� criados(Post object).
 - T�tulo: A maior Cobertura do UFC e Pr�ximos Eventos Exclusivos.
5- Para visualizar estes posts digite na barra de endere�os: http://127.0.0.1:8000/lista-todos/
Onde al�m de atualizar, poder� fazer a dele��o dos posts(ao lado de cada posts), tamb�m poder� criar um novo post na barra de 
endere�os:http://127.0.0.1:8000/novo/, implantado nas urls e models.
