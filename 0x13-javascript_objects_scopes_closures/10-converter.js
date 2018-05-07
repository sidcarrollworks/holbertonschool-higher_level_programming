#!/usr/bin/node
exports.converter = function (base) {
  this.base = base;
  function converter (number) {
    return number.toString(this.base);
  }
  return converter;
};
