#!/usr/bin/node
// Get the first argument passed to the script
// Print the first argument, or a message if no argument was passed

const { argv } = require('process');
console.log(argv[2] + ' is ' + argv[3]);
