let actors = require('./actor1441.json');
let movies = require('./movie2.json');
let directors = require('./director1441.json');

for (let i =0; i < movies.length; i++) {
    let movie =  movies[i];
    let movie_id = movie.fields.movie_id
    actors.forEach(function(actor, index) {
         let actormovie_id = actor.fields.movies
         if (actormovie_id === movie_id) {
             movie.fields.actors.push(actor.pk);
         }
    })
}
for (let i =0; i < movies.length; i++) {
    let movie =  movies[i];
    let movie_id = movie.fields.movie_id
    directors.forEach(function(actor, index) {
         let actormovie_id = actor.fields.movies
         if (actormovie_id === movie_id) {
             movie.fields.directors.push(actor.pk);
         }
    })
}
movies.forEach(function(movie) {
    delete movie.fields.movie_id;
})
const fs = require('fs');

let data = JSON.stringify(movies);
fs.writeFileSync('movieresult.json', data);