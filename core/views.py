from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm

@login_required(login_url='/admin/login/')
def dashboard(request):
    # Vai buscar apenas os chamados do utilizador com sessão iniciada
    tickets = Ticket.objects.filter(cliente=request.user)
    
    # Fazer as contas reais utilizando a base de dados
    total = tickets.count()
    abertos = tickets.filter(status__in=['aberto', 'atendimento']).count()
    resolvidos = tickets.filter(status='resolvido').count()
    
    # Empacota tudo para enviar para o HTML
    context = {
        'tickets': tickets,
        'total': total,
        'abertos': abertos,
        'resolvidos': resolvidos,
    }
    
    return render(request, 'core/dashboard.html', context)

@login_required(login_url='/admin/login/')
def novo_chamado(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.cliente = request.user # Associa o chamado a quem tem a sessão iniciada
            ticket.save()
            return redirect('dashboard') # Volta para o dashboard depois de guardar
    else:
        form = TicketForm()
        
    return render(request, 'core/novo_chamado.html', {'form': form})