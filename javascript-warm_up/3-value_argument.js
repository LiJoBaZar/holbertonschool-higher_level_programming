#!/usr/bin/node
// Get the first argument passed to the script
// Print the first argument

const { firstArg } = require('process');
if (!firstArg[2]){
  console.log('No argument');
}
if (firstArg[2]) {
  console.log(firstArg[2]);
}
