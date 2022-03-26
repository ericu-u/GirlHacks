
var document.getElementById()


function refreshChart() {

}

window.onload = function() {
    var refreshInterval = 3000;

    var chartData = {
        labels: ['Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5', 'Sensor 6', 'Sensor 7'],
        datasets: [{
            label: 'Sensor Data',
            data: [10, 13, 12, 11, 13, 19, 12]
        }]
    };
    
    var chartOptions = {
        title: {
            display: true, // defaults to false
            text: "Bar Chart with Dynamic Data",
            fontSize: 45,
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    };

    var ctx = document.getElementById('chartCanvas').getContext('2d');

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: chartOptions
    });

    setInterval(function(){
        console.log("Update Chart");
        var dps = chartData.datasets[0].data;
        for(var i = 0; i < dps.length; i++) {
            dps[i] += getRandomInt(-10, 10);
        }
        
        myChart.update();
    }, refreshInterval);
}