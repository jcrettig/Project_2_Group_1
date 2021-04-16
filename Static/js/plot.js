const imdb = "http://127.0.0.1:5000/api/v1.0/imdb"

var button = d3.select("#submitBtn")  
function buildPlot() {
  d3.json(imdb).then(function(data) {
    console.log(data)
 

  var inputValue_x = d3.select("#x-selector-dropdown")
  var inputValue_y = d3.select("#y-selector-dropdown")

  var searchValue_x = inputValue_x.property("value")
  var searchValue_y = inputValue_y.property("value")
 
    var trace1 = {
      mode: "markers",
      type: "scatter",
      x: data[searchValue_x],
      y: data[searchValue_y],
    }
  
    var chartdata = [trace1]
  
    var layout = {
      xaxis: { title: searchValue_x },
      yaxis: { title: searchValue_y}
    }
    Plotly.newPlot("plot", chartdata, layout)
  })
}
    
button.on("click", buildPlot)  