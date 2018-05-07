#!/usr/bin/node
let total = -1;
exports.logMe = function (item) {
  total++;
  console.log(total + ': ' + item);
};
