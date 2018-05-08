#!/usr/bin/node
let request = require('request');
request
  .get('http://swapi.co/api/people/18', (err, res, body) => {
    if (err) throw err;
    console.log(JSON.parse(body).films.length);
  });
