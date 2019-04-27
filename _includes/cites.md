
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">
</script>
<script type="text/javascript" src="http://code.highcharts.com/highcharts.js">
</script>
<script type="text/javascript" src="http://code.highcharts.com/modules/exporting.js">
</script>

<div id="container" style="min-width: 500px; height: 400px; margin: 0 auto"> 
</div>
<script type="module">
    import Highcharts from "https://code.highcharts.com/es-modules/masters/highcharts.src.js";
    Highcharts.chart("container", {
            chart: {
                type: "column" 
            }, 
            credits : { enabled : false },
            title: {
                text: "Recent citations",
            },
            xAxis: {
                categories: ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
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
                data : [5, 6, 38, 62, 110, 189, 185, 211, 70],
                yAxis : 0
              },
              {
                name : "papers", 
                data : [5, 2, 3, 1, 2, 3, 2, 2, 3], 
                yAxis : 1
              }
            ]
        });
</script>

