from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import json
from .models import Ticket, TicketLog
from .forms import TicketForm

@login_required(login_url='login')
def dashboard(request):
    tickets = Ticket.objects.filter(cliente=request.user)
    
    total = tickets.count()
    abertos = tickets.filter(status__in=['aberto', 'atendimento']).count()
    resolvidos = tickets.filter(status='resolvido').count()
    
    # === LÓGICA DO GRÁFICO ===
    categorias_count = tickets.values('categoria').annotate(total=Count('categoria'))
    dict_categorias = dict(Ticket.CATEGORIA_CHOICES)
    
    labels = []
    data = []
    
    for item in categorias_count:
        nome_categoria = dict_categorias.get(item['categoria'], item['categoria'])
        labels.append(nome_categoria)
        data.append(item['total'])
        
    context = {
        'tickets': tickets,
        'total': total,
        'abertos': abertos,
        'resolvidos': resolvidos,
        # Enviando os dados do gráfico pro HTML
        'chart_labels': json.dumps(labels) if labels else '["Sem chamados"]',
        'chart_data': json.dumps(data) if data else '[1]',
    }
    
    return render(request, 'core/dashboard.html', context)

@login_required(login_url='login')
def novo_chamado(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.cliente = request.user
            ticket.save()
            return redirect('dashboard')
    else:
        form = TicketForm()
        
    return render(request, 'core/novo_chamado.html', {'form': form})

@login_required(login_url='login')
def detalhes_chamado(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    
    if not request.user.is_staff and ticket.cliente != request.user:
        return redirect('dashboard')

    if request.method == 'POST':
        novo_status = request.POST.get('status')
        if novo_status and novo_status != ticket.status:
            status_antigo = ticket.get_status_display()
            ticket.status = novo_status
            ticket.save()
            
            TicketLog.objects.create(
                ticket=ticket,
                acao=f"Status alterado de '{status_antigo}' para '{ticket.get_status_display()}'",
                usuario=request.user
            )
            return redirect('detalhes_chamado', id=ticket.id)

    historico = ticket.historico.all()
    return render(request, 'core/detalhes_chamado.html', {'ticket': ticket, 'historico': historico})