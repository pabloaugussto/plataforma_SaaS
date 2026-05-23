from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo', 'categoria', 'prioridade', 'descricao']
        
        # Aqui é onde a magia acontece: injetamos o CSS do nosso Dark Mode!
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: O sistema não está a iniciar...'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'prioridade': forms.Select(attrs={
                'class': 'form-control'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5, 
                'placeholder': 'Detalhe o problema com o máximo de informações possível...'
            }),
        }