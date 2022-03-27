
// var  document.getElementById()

function refreshChart() {

}

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
        title: {
            display: true, // defaults to false
            text: "Bar Chart with Dynamic Data",
            fontSize: 45,
        },
        scales: {
            y: {
                beginAtZero: true
            }
        },
        responsive: false,
    };

    var ctx = document.getElementById('weightloss-chart').getContext('2d');

    var myChart = new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: chartOptions
    });
        
    myChart.update();

}