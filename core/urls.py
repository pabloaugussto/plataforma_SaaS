from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('novo/', views.novo_chamado, name='novo_chamado'),  
]