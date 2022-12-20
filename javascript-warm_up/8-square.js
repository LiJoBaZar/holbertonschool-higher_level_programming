#!/usr/bin/node
// Tis a script in JavaScript that prints a square of a given size using the character X

const size = process.argv[2];
if (!size || isNaN(size)) {
  console.log("Missing size");
return;
}
size = parseInt(size, 10);
for (let i = 0; i < size; i++) {
let row = 'X';
for (let j = 0; j < size; j++) {
  row += 'X';
}
  console.log(row);
}
