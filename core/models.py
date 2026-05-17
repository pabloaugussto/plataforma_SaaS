from django.db import models
from django.contrib.auth.models import User

class Ticket (models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('atendimento', 'Em Atendimento'),
        ('resolvido', 'Resolvido'),
        ('fechado', 'Fechado'),
    ]

    PRIORITY_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'), 
        ('alta', 'Alta'),
    ]

    CATEGORIA_CHOICES = [
        ('software', 'Problema de Software / Bug'),
        ('hardware', 'Problema de Hardware'),
        ('acesso', 'Acessos e Permissões'),
        ('financeiro', 'Financeiro e Faturamento'),
        ('outros', 'Outros Assuntos'),
    ]

    titulo = models.CharField(max_length=150, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição do Problema")
    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICES, default='software')
    prioridade = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='media')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='aberto')

    # Relacionamentos
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chamados_criados')
    tecnico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='chamados_atendidos')

    # Datas
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-data_criacao']
        verbose_name = "Chamado"
        verbose_name_plural = "Chamados"

    def __str__(self):
        return f"#{self.id} - {self.titulo} ({self.get_status_display()})"
