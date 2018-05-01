#!/usr/bin/node
const num = parseInt(process.argv[2]);
const answer = (function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
})(num);
console.log(answer);
