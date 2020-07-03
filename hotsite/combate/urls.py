from django.conf.urls import url
from combate.views import lista,novo,atualiza,deletar

urlpatterns=[
       
        url(r'^lista-todos/$',lista,name='lista_todos'),
        url(r'^novo/$',novo),
        url(r'^atualizar/(?P<id>\d+)/$',atualiza,name='atualizar'),
        url(r'^deletar/(?P<id>\d+)/$',deletar,name='deletar'),
]
 
