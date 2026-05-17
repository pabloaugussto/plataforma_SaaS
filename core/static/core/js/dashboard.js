document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('chamadosChart').getContext('2d');
    
    // Nossas cores modernas
    const orangeColor = '#f97316'; 
    const darkBlueColor = '#0f172a';
    const lightBlue = '#3b82f6';
    const grayColor = '#cbd5e1';
    const greenColor = '#22c55e';

    // Pegamos as variáveis dinâmicas que o Django mandou pelo HTML
    // Se, por algum motivo falhar, usamos um padrão vazio
    const labelsValues = typeof chartLabels !== 'undefined' ? chartLabels : ['Nenhum'];
    const dataValues = typeof chartData !== 'undefined' ? chartData : [1];

    // Se só tiver "Sem chamados", o gráfico fica todo cinza
    const backgroundColors = labelsValues[0] === 'Sem chamados' 
        ? [grayColor] 
        : [orangeColor, darkBlueColor, lightBlue, greenColor, grayColor];

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labelsValues,
            datasets: [{
                data: dataValues,
                backgroundColor: backgroundColors,
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
            cutout: '75%'
        }
    });
});