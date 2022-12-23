#!/usr/bin/node

const second = [0, 0];
let secondSorted;

for (let i = 2; i < process.argv.length; i++) {
	  second[i] = parseInt(process.argv[i]);
}
secondSorted = second.sort(function (a, b) { return a - b; });
secondSorted = secondSorted.reverse();

console.log(secondSorted[1]);
