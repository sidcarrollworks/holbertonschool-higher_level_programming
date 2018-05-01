#!/usr/bin/node
let num = process.argv.length - 2;
if (num === 0) {
  console.log('No argument');
} else if (num === 1) {
  console.log('Argument found');
} else if (num >= 1) {
  console.log('Arguments found');
}
