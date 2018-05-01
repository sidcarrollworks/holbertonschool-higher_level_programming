#!/usr/bin/node
let arr = process.argv.slice(2).map(x => parseInt(x));
if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  let max = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(max), 1);
  console.log(Math.max.apply(null, arr));
}
