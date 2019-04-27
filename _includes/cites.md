<div id="cites" style="min-width: 500px; height: 400px; margin: 0 auto"> 
</div>
<script type="module">
//    import Highcharts from "https://code.highcharts.com/es-modules/masters/highcharts.src.js";
    Highcharts.chart("cites", {
            chart: {
                type: "column" 
            }, 
            credits : { enabled : false },
            title: {
                text: "benchmark",
            },
            xAxis: {
                categories: [ '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
            },
            yAxis: [
               {
                title: {
                    text: "citations"
                },
              },
              {
                title: {
                    text: "publications"
                },
                opposite : true,
                allowDecimals: false,
              }],
            series: [
              { 
                name : "Citations", 
                data : [0, 0, 5, 6, 38, 62, 110, 189, 185, 211, 70],
                yAxis : 0
              },
              {
                name : "papers", 
                data : [1, 1, 0, 2, 6, 3, 6, 2, 2, 1, 0], 
                yAxis : 1
              }
            ]
        });
</script>

