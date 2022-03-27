
// var  document.getElementById()

window.onload = function() {
    var chartData = {
        labels: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', ],
        datasets: [{
            label: 'Weight Over Time',
            data: [10, 13, 12, 11, 13, 19, 12],
            borderColor: 'red',
        }]
    };
    
    var chartOptions = {
        plugins: {
            title: {
                display: true, // defaults to false
                text: "Line Chart of Weight over the Week",
                fontSize: 40,
            },
            legend: {
                fullSize: false,
            },
        },
        
        scales: {
            x: {
                title: {
                    text: 'Day of the Week',
                    display: true,
                }
            },
            y: {
                beginAtZero: true,
                title: {
                    text: 'Weight',
                    display: true,
                }
            }
        },
        responsive: false,
        maintainAspectRatio: false,
    };

    var ctx = document.getElementById('weightloss-chart').getContext('2d');

    var myChart = new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: chartOptions
    });

    myChart.update();
}
