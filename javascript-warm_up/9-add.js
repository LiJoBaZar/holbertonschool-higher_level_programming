#!/usr/bin/node
// You can call the function by passing in two integers as arguments, and the function will print the sum of those integers to the console.

const { argv } = require('process');
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

add(a, b);

function add (a, b) {
  const result = a + b;
  console.log(result);
}
