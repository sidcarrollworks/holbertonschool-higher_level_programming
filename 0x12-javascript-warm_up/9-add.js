#!/usr/bin/node
let answer = (function add (a, b) {
  return parseInt(a) + parseInt(b);
})(process.argv[2], process.argv[3]);
console.log(answer);
