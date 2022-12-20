#!/usr/bin/node
// This a script that computes and prints the factorial of an integer using recursion

const { argv } = require('process');
const n = parseInt(argv[2]);

console.log(factorial(n));

function factorial (n) {
  if (!n) {
    return 1;
  }
  return n * factorial(n - 1);
}
