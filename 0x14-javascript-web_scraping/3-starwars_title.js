#!/usr/bin/node
let request = require('request');
request
  .get('http://swapi.co/api/films/' + process.argv[2],
    (err, res, body) => {
      if (err) throw err;
      console.log(JSON.parse(body).title);
    });
