// Variable set up
const imdb = "http://127.0.0.1:5000/api/v1.0/imdb"
const imdbDonut = "http://127.0.0.1:5000/api/v1.0/imdb2"
var imdbTitleArray = "http://127.0.0.1:5000/api/v1.0/imdb_title"

var buttonPlot = d3.select("#submitBtn")  
var buttonDonut = d3.select("#submitBtnDonut") 
var plotDonut = d3.select("#plotDonut")
var donutDropdown =  d3.select('#x-selector-dropdown-donut')

// Change Title Case
function toTitleCase(str) {
  str = str.replace("_", " ")
  return str.replace(/\w\S*/g, function(txt){
      return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
  });
}

// Create a list of movies to append to movies donut dropdown
d3.json(imdbTitleArray).then(data => {
  data.forEach(movie => {
    donutDropdown.append("option").text(toTitleCase(movie)).property("value", movie)
  })
});


// Render original charts

// Default Scatter
var scatterLoad = (defaultScatter => { 
	d3.json(imdb).then(data => {
    var xAxis = data.usa_gross
    var yAxis = data.year

    var movieTitle = data.title

    var xTitle = `USA Gross Profit`
    var yTitle =  `Year`
    var chartTitle = `Scatter Comparison: ${xTitle} vs. ${yTitle}`
  
    var trace1 = {
      mode: "markers", 
      type: "scatter",
      x: xAxis,
      y: yAxis,
      text: movieTitle
    }
  
    var chartdata = [trace1]
  
    var layout = {
      title: {
        text: chartTitle
      },
      xaxis: { title: xTitle },
      yaxis: { title: yTitle }
    }

    Plotly.newPlot("plot", chartdata, layout)
  })
});

// Load original scatter plot
scatterLoad()

// Default Donut Chart
var donutLoad = (defaultDonut => {
  d3.json(imdbDonut).then(data => {

    // set default movie title
    var searchMovie = 'black panther';

    // filter through data to find title
    var movieTitle = data.filter(movie => movie.title === searchMovie)
    console.log(movieTitle)
    // grab USA and world gross for title
    var movieUSA = movieTitle[0]['usa_gross']
    var movieWorld = movieTitle[0]['world_gross']

    var movieData = [
      {x: "USA Gross", value: movieUSA},
      {x: "World Gross", value: movieWorld}
    ]
    // create pie chart, set data
    chart = anychart.pie(movieData);

    /* set the inner radius(to turn the pie chart into a doughnut chart)*/
    chart.innerRadius("35%");

    // set the position of labels
    chart.labels().position("outside");

    // configure connectors
    chart.connectorStroke({color: "#595959", thickness: 2, dash:"2 2"});

    // set the container id
    chart.container("plotDonut");

    // create and configure a label
    var label = anychart.standalones.label();
    label.text("Black Panther");
    label.width("100%");
    label.height("100%");
    label.fontColor("#60727b");
    label.hAlign("center");
    label.vAlign("middle");

    // set the label as the center content
    chart.center().content(label);

    // initiate drawing the chart
    chart.draw();
  })
})

// Load default donut chart 
donutLoad()


// Build Scatter Plot
function buildPlot() {
  d3.json(imdb).then(function(data) {

  var inputValue_x = d3.select("#x-selector-dropdown")
  var inputValue_y = d3.select("#y-selector-dropdown")

  var searchValue_x = inputValue_x.property("value")
  var searchValue_y = inputValue_y.property("value")
  

  var movieTitle = data.title

  var xTitle = toTitleCase(searchValue_x)
  var yTitle = toTitleCase(searchValue_y)
  var chartTitle = `Scatter Comparison: ${xTitle} vs. ${yTitle}`

    var trace1 = {
      mode: "markers", 
      type: "scatter",
      x: data[searchValue_x],
      y: data[searchValue_y],
      text: movieTitle
    }
  
    var chartdata = [trace1]
  
    var layout = {
      title: {
        text: chartTitle
      },
      xaxis: { title: xTitle },
      yaxis: { title: yTitle }
    }
    Plotly.newPlot("plot", chartdata, layout)
  })
}

// Donut Chart
var buildDonut = (buildDonut => {
  d3.json(imdbDonut).then(data => {
    console.log(data)

    // clear the previous graph 
    plotDonut.html("");

    // reference html element, get searched title
    var inputMovie = d3.select("#x-selector-dropdown-donut");
    var searchMovie = inputMovie.property("value");


    // filter through data to find searched title
    var movieTitle = data.filter(movie => movie.title === searchMovie)
    console.log(movieTitle)
    // grab USA and world gross for searched title
    var movieUSA = movieTitle[0]['usa_gross']
    var movieWorld = movieTitle[0]['world_gross']

    var movieData = [
      {x: "USA Gross", value: movieUSA},
      {x: "World Gross", value: movieWorld}
    ]
    // create pie chart, set data
    chart = anychart.pie(movieData);

    /* set the inner radius(to turn the pie chart into a doughnut chart)*/
    chart.innerRadius("30%");

    // set the position of labels
    chart.labels().position("outside");

    // configure connectors
    chart.connectorStroke({color: "#595959", thickness: 2, dash:"2 2"});

    // create and configure a label
    var label = anychart.standalones.label();
    label.text(movieTitle[0]['title']);
    label.width("100%");
    label.height("100%");
    label.fontColor("#60727b");
    label.hAlign("center");
    label.vAlign("middle");

    // set the label as the center content
    chart.center().content(label);

    // set the container id
    chart.container("plotDonut");

    // initiate drawing the chart
    chart.draw();
  })
})


// create event listener
buttonPlot.on("click", buildPlot)  
buttonDonut.on("click", buildDonut)



// d3.selectAll('#x-selector-dropdown-donut').on('change', buildDonut)

