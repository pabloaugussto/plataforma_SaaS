document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('chamadosChart').getContext('2d');
    
    // Pegamos a cor laranja direto do CSS
    const orangeColor = '#f97316'; 
    const darkBlueColor = '#0f172a';

    new Chart(ctx, {
        type: 'doughnut', // Gráfico de rosca
        data: {
            labels: ['Software', 'Hardware', 'Acesso', 'Financeiro'],
            datasets: [{
                data: [45, 25, 20, 10], // Dados fictícios por enquanto
                backgroundColor: [
                    orangeColor,
                    darkBlueColor,
                    '#3b82f6', // Azul claro
                    '#cbd5e1'  // Cinza
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                }
            },
            cutout: '75%' // Deixa a rosca mais fina e moderna
        }
    });
});