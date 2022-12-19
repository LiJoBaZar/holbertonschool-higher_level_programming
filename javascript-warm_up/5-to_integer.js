#!/usr/bin/node
// Get the first and second arguments passed to the script
// Print the two arguments in the specified format, or a message if no arguments were passed

const { argv } = require('process');
const n = parseInt(argv[2]);
if (isNaN(n)) {
  console.log('Not a number');
}
else {
  console.log('My number: ' + n);
}
