#!/usr/bin/node
// Get the first argument passed to the script
// Print the first argument

const { argv } = require('process');
if (!argv[2]){
  console.log('No argument');
}
if (argv[2]) {
  console.log(argv[2]);
}
