Highcharts.chart('linearchart', {
    chart: {
        type: 'line'
    },
    title: {
        text: 'Cantidad de Actividades por Día'
    },
    xAxis: {
        categories: [],
        title: {
            text: 'Días'
        }
    },
    yAxis: {
        title: {
            text: 'Cantidad de Actividades'
        }
    },
    series: [{
        name: 'Actividades',
        data: []
    }]
});

Highcharts.chart('piechart', {
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Total de Actividades por Tipo'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Actividades',
        colorByPoint: true,
        data: []
    }]
});

Highcharts.chart('columnchart', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Cantidad de Actividades por Mes y Hora'
    },
    xAxis: {
        categories: [],
        title: {
            text: 'Meses'
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Cantidad de Actividades'
        }
    },
    series: [{
        name: 'Mañana',
        data: []
    }, {
        name: 'Medio Día',
        data: []
    }, {
        name: 'Tarde',
        data: []
    }]
});

fetch("http://127.0.0.1:5000/obtener_stats")
  .then((response) => response.json())
  .then((data) => {
    console.log("Datos recibidos:", data);

    const fechas_lc = data.actividades_por_dia.map(item => item.dia);
    const cantidades_lc = data.actividades_por_dia.map(item => item.cantidad);

    const tipos_pc = data.actividades_por_tipo.map(item => item.tipo);
    const cantidades_pc = data.actividades_por_tipo.map(item => item.cantidad);

    const meses = data.actividades_por_mes_mañana.map(item => item.mes);
    const cantidadesMañana = data.actividades_por_mes_mañana.map(item => item.cantidad);
    const cantidadesMedioDia = data.actividades_por_mes_mediodia.map(item => item.cantidad);
    const cantidadesTarde = data.actividades_por_mes_tarde.map(item => item.cantidad);

    // Get the linechart by ID
    const linechart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "linearchart"
    );

    // Update the chart with new data
    linechart.update({
      xAxis: {
        categories: fechas_lc,
      },
    });

    linechart.update({
      series: [
        {
          data: cantidades_lc,
        },
      ],
    });

    // Get the piechart by ID
    const piechart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "piechart"
    );
    // Update the pie chart with new data
    piechart.update({
        series: [{
            data: tipos_pc.map((tipo, index) => ({
            name: tipo,
            y: cantidades_pc[index]
            }))
        }]
    });

    // Get the columnchart by ID
    const columnchart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "columnchart"
    );
    // Update the column chart with new data
    columnchart.update({
      xAxis: {
        categories: meses,
      },
    });

    columnchart.update({
      series: [
        {
          name: 'Mañana',
          data: cantidadesMañana
        },
        {
          name: 'Medio Día',
          data: cantidadesMedioDia
        },
        {
          name: 'Tarde',
          data: cantidadesTarde
        }
      ]
    });

  })
  .catch((error) => console.error("Error:", error));

