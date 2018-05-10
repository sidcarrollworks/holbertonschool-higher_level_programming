$.get('https://swapi.co/api/films/?format=json', (data) => {
  const movies = data.results;
  movies.forEach(movie => {
    let title = movie.title;
    $('#list_movies').append(`<li>${title}</li`);
  });
});
