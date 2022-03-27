

// Function to create chart
function LoadChart(labels, label, data, canvas, title) {
    var chartData = {
        labels: labels,
        datasets: [{
            label: label,
            data: data,
            borderColor: 'red',
        }]
    };
    var chartOptions = {
        plugins: {
            title: {
                display: true, // defaults to false
                text: title,
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
    var ctx = document.getElementById(canvas).getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: chartOptions
    });
    myChart.update();
}

// Using AJAX requests to obtain data from APIs
function loadWeight() {
    $.ajax({
        type: 'GET',
        url: "/api/weight",
        success: function (response) {
            // get data from request and update chart
            labels = response['weeks']
            label = 'Weight Over Time'
            data = response['data']
            LoadChart(labels, label, data, 'chart1', "Line Chart of Weight over Weeks")
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Weight Data Error");
        }
    })
}
function loadHeight() {
    $.ajax({
        type: 'GET',
        url: "/api/height",
        success: function (response) {
            // get data from request and update chart
            labels = response['weeks']
            label = 'Average Sleep'
            data = response['data']
            LoadChart(labels, label, data, 'chart2', "Line Chart of Sleep over Weeks")
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Height Data Error");
        }
    })
}
function loadBMI() {
    $.ajax({
        type: 'GET',
        url: "/api/BMI",
        success: function (response) {
            // get data from request and update chart
            labels = response['weeks']
            label = 'BMI Over Time'
            data = response['data']
            LoadChart(labels, label, data, 'chart3', "Line Chart of BMI over Weeks")
        },
        error: function (response) {
            // alert the error if any error occured
            alert("BMI Data Error");
        }
    })
}

// Load default data on page load
window.onload = loadWeight()
window.onload = loadHeight()
window.onload = loadBMI()

// Obtaining buttons to establish event listeners
buttonHeight = document.getElementById("chart-height")
buttonWeight = document.getElementById("chart-weight")
buttonBMI = document.getElementById("chart-bmi")

// Obtaining charts to display
chart1 = document.getElementById('chart1')
chart2 = document.getElementById('chart2')
chart3 = document.getElementById('chart3')

// Assinging Displays
buttonBMI.addEventListener("click", () => {
    chart1.style.display = 'none'
    chart2.style.display = 'none'
    chart3.style.display = 'block'
})
buttonHeight.addEventListener("click", () => {
    chart1.style.display = 'none'
    chart3.style.display = 'none'
    chart2.style.display = 'block'
})
buttonWeight.addEventListener("click", () => {
    chart3.style.display = 'none'
    chart2.style.display = 'none'
    chart1.style.display = 'block'
})