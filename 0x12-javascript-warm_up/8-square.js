#!/usr/bin/node
let size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let n = parseInt(size);
  for (let i = 0; i < n; i++) {
    console.log('X'.repeat(n));
  }
}
