from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('validar_cadastro/', views.validar_cadastro, name='validar_cadastro'),
    path('login/', views.login, name='login'),
    path('validar_login/', views.validar_login, name='validar_login'),
    path('esqueceu_senha/', views.esqueceu_senha, name='esqueceu_senha'),
    path('validar_esqueceu_senha/', views.validar_esqueceu_senha, name='validar_esqueceu_senha'),
    path('sair/', views.sair, name='logout')
]
