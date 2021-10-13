from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agradecimento', views.agradecimento, name="agradecimento"),
    path('login', views.login, name="login"),
    path('email_clientes', views.email_clientes, name='email_clientes')
]