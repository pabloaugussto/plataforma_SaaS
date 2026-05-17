from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('novo/', views.novo_chamado, name='novo_chamado'),
    path('chamado/<int:id>/', views.detalhes_chamado, name='detalhes_chamado'),  
]