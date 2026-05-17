from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'categoria', 'prioridade', 'status', 'data_criacao']
    list_filter = ['status', 'prioridade', 'categoria']
    search_fields = ['titulo', 'descricao', 'cliente__username']
                    


