#!/usr/bin/node
// Tis an example script that prints "C is fun"

const { argv } = require('process');
const n = parseInt(argv[2]);

if (!n) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < n; i++) {
  console.log('C is fun');
}
