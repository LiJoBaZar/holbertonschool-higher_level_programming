#!/usr/bin/node
const { argv } = require('process');
// Get the number of arguments passed to the script
// Print a message depending on the number of arguments

if (argv.length > 3) {
console.log('No arguments');
} 
if (argv.length === 3) {
console.log('Arguments found');
}
if (argv.length < 3){
console.log('Arguments found');
}