from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('novo/', views.novo_chamado, name='novo_chamado'),
    path('chamado/<int:id>/', views.detalhes_chamado, name='detalhes_chamado'),  
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
]