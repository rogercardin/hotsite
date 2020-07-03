Passo a Passo para rodar a aplicacao
-Instalação do Pyhton e as variáveis de ambiente no windows
-Usando o Django que é um Framework baseado na linguagem Python
-Framework rápido e escalável, excelente performace.
-Baseado em arquitetura MTV
-Models(Classes e Objetos e camada de acesso aos dados ao BD)
-View(Controllers do MTV, comunicação entre o template e o Model)
-URL'S(Define as rotas ou seja para onde irá suas requisições e respostas(request e response)
-Templates(Equivalente as views e arquivos estáticos)
-Baseados em aplicaçoes(pode reusar as suas aplicações)
-Adminitração com um Painel Admnistrativo com soluções rápidas (Django Admin)
-Instalação no windows
Dentro do terminal do python:
Abra a interface IDLE(Python GUI)
Digite django-admin startproject hotsite
A estrutura do projeto hotsite:
diretorios: hotsite,combate,manage
-No sub-diretório hotsite: Definição da estrutura com arquivos em .py(settings,admin,urls,wsgi)
-settings: configuraçoes: STATIC_URL:'/static/' 
ROOT_URLCONF:'hotsite.urls'
INSTALLED_APPS:'combate'
DATABASES:Definisdas dentro do servidor local wampp64
'ENGINE': 'django.db.backends.mysql'
'NAME': 'combate'
'USER': 'root'
'PASSWORD': '',
    
-No sub-diretório combate: Definição de arquivos estáticos, templates, admin,forms, models,urls.
Models: Modelo do BD(Com a Classe Post, também são definidas as tabelas que serão criadas dinamicamente)
URLS's (definição das URLS's do sistema como: lista-todos,novo)
VIEWS(São os controles da aplicação, definidos como lista,novo,atualizar e deletar(CRUD)
Templates(localizados os arquivos em html com css e javascript e utilização do BootstrapCDN)

Execução:

1-Digite o cmd no Windows e na pasta hotsite digite: cd hotsite e dentro dele o comando do python manage.py validate
e depois manage.py runserver para conectar o servidor.
2- Na Barra de endereços: digite a seguinte URL:http://127.0.0.1:8000/admin/ para entrar no Painel Administrativo do Django
3- Para fazer login na aplicação digite login: admin e password: 123456
4- O sistema apresentará a tela de Combate administration com os Posts já criados(Post object).
 - Título: A maior Cobertura do UFC e Próximos Eventos Exclusivos.
5- Para visualizar estes posts digite na barra de endereços: http://127.0.0.1:8000/lista-todos/
Onde além de atualizar, poderá fazer a deleção dos posts(ao lado de cada posts), também poderá criar um novo post na barra de 
endereços:http://127.0.0.1:8000/novo/, implantado nas urls e models.
