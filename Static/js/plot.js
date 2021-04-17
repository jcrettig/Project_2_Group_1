const imdb = "http://127.0.0.1:5000/api/v1.0/imdb"
var imdbDonut = "http://127.0.0.1:5000/api/v1.0/imdb2"
// var tomato = "http://127.0.0.1:5000/api/v1.0/tomato"

var buttonPlot = d3.select("#submitBtn")  
var buttonDonut = d3.select("#submitBtnDonut") 

function buildPlot() {
  d3.json(imdb).then(function(data) {
    console.log(data)

  var inputValue_x = d3.select("#x-selector-dropdown")
  var inputValue_y = d3.select("#y-selector-dropdown")

  var searchValue_x = inputValue_x.property("value")
  var searchValue_y = inputValue_y.property("value")

  var movieTitle = data.title
  var chartTitle = `${searchValue_x} vs. ${searchValue_y}`

  // TODO
  var xTitle = searchValue_x
  var yTitle = searchValue_y

    var trace1 = {
      mode: "markers",
      type: "scatter",
      x: data[searchValue_x],
      y: data[searchValue_y],
      text: movieTitle
    }
  
    var chartdata = [trace1]
  
    // TODO
    var layout = {
      title: { title_text: chartTitle },
      xaxis: { title: xTitle },
      yaxis: { title: yTitle }
    }
    Plotly.newPlot("plot", chartdata, layout)
  })
}

// Donut Chart
function buildDonut() {
  d3.json(imdbDonut).then(data => {
    console.log(data)

    // reference html element, get searched title
    var inputMovie = d3.select("#searchTitle");
    var searchMovie = inputMovie.property("value").toLowerCase();

    // filter through data to find searched title
    var movieTitle = data.filter(movie => movie.title === searchMovie)
    console.log(movieTitle)
    
    // grab USA and world gross for searched title
    var movieUSA = movieTitle[0]['usa_gross']
    var movieWorld = movieTitle[0]['world_gross']

    console.log(movieUSA)
    console.log(movieWorld)

    var movieData = [
      {x: "USA Gross", value: movieUSA},
      {x: "World Gross", value: movieWorld}
    ]
    // create pie chart, set data
    chart = anychart.pie(movieData);

    /* set the inner radius(to turn the pie chart into a doughnut chart)*/
    chart.innerRadius("30%");

    // set the container id
    chart.container("plotDonut");

    // initiate drawing the chart
    chart.draw();
  })
}

buttonPlot.on("click", buildPlot)  
buttonDonut.on("click", buildDonut)