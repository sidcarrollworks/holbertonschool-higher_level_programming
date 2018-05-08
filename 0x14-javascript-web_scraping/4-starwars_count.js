#!/usr/bin/node
let request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) throw err;
  let data = JSON.parse(body);
  let count = 0;
  let movies = data.results;
  let urls = 'https://swapi.co/api/people/18/';
  let url = 'http://swapi.co/api/people/18/';
  for (let i = 0; i < movies.length; i++) {
    for (let x = 0; x < movies[i].characters.length; x++) {
      if (movies[i].characters[x] === url || movies[i].characters[x] === urls) {
        count += 1;
      }
    }
  }
  console.log(count);
});
