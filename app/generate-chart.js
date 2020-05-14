
const generateChart = (data, algoName) => {
    const elem = $(`#performance-chart`);
    let x = [];
    let y = [];
    data.forEach(point => {
        x.push(point.x);
        y.push(point.y);
    });
    const performanceChart = new Chart(elem, {
        type: 'line',
        data: {
            labels: y,
            datasets: [
                {
                    data: x,
                    label: 'Portfolio Value',
                    fontColor: '#ffffff',
                    borderColor: '#11998e',
                    fill: true
                }
            ] 
        },
        options: {
            title: {
                display: true,
                text: `Performance for ${algoName}`,
                fontSize: 18,
                fontColor: '#ffffff'
            },
            scales: {
                xAxes: [{
                    ticks: {
                        fontColor: '#ffffff'
                    }
                }],
                yAxes: [{
                    ticks: {
                        fontColor: '#ffffff',
                        callback: function(value, index, values) {
                            if(parseInt(value) >= 1000){
                              return '$' + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                            } else {
                              return '$' + value;
                            }
                        }
                    }
                }]

            }
        } 
    }); 
};

const testChartLoad = () => {
    generateChart([
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'Jan'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'Feb'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'Mar'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'Apr'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'May'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'June'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'Jul'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'Aug'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'Sep'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'Oct'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'Nov'
        },
        {
            x: Math.floor((Math.random() * 120000) + 90000),
            y: 'Dec'
        }
    ], 'SMABot.py');
}

// module.exports.testChartLoad = testChartLoad;
testChartLoad();
