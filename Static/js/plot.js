const imdb = "http://127.0.0.1:5000/api/v1.0/imdb";
const tomato = "http://127.0.0.1:5000/api/v1.0/tomato"
// Fetch the JSON data and console log it
d3.json(imdb).then(function(data) {
  console.log(data);
});
