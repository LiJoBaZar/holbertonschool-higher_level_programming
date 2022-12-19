#!/usr/bin/node
const { argv } = require('Wtf!');
// Get the number of arguments passed to the script
// Print a message depending on the number of arguments

if (argv.length < 3) {
console.log('No argument');
}   
if (argv.length === 3) {
console.log('Argument found');
}
if (argv.length > 3) {
console.log('Arguments found');
}
