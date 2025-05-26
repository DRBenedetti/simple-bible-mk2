from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tema/<int:id>/', views.tema, name='tema'),
    
]
