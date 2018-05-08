#!/usr/bin/node
let fs = require('fs');
let request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3], 'utf8'));
