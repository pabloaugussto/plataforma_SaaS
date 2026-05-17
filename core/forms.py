from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # Definimos quais campos do nosso Model vão aparecer para o cliente preencher
        fields = ['titulo', 'descricao', 'categoria', 'prioridade']
        
        # Aqui customizamos o HTML de cada campo para que eles usem o visual moderno do nosso CSS
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: Erro ao acessar a tela de relatórios'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'prioridade': forms.Select(attrs={
                'class': 'form-control'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Detalhe o problema que você está enfrentando...'
            }),
        }