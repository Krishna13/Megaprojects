/*=========================================================================================
    File Name: doughnut.js
    Description: Chartjs simple doughnut chart
    ----------------------------------------------------------------------------------------
    Item Name: Robust - Responsive Admin Theme
    Version: 1.2
    Author: PIXINVENT
    Author URL: http://www.themeforest.net/user/pixinvent
==========================================================================================*/

// Doughnut chart
// ------------------------------
$(window).on("load", function() {

    //Get the context of the Chart canvas element we want to select
    var ctx = $("#simple-doughnut-chart");

    // Chart Options
    var chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        // responsiveAnimationDuration: 500,
    };

    // Chart Data
    var chartData = {
        labels: ["January", "February", "March", "April", "May"],
        datasets: [{
            label: "My First dataset",
            data: [66, 35, 24, 45, 85],
            backgroundColor: ["#00bbf0", "#ff6f3c", "#ffc93c", "#ff9a3c", "#155263"],
        }]
    };

    var config = {
        type: 'doughnut',

        // Chart Options
        options: chartOptions,

        data: chartData
    };

    // Create the chart
    var doughnutSimpleChart = new Chart(ctx, config);

});