#!/usr/bin/node

const myVar = 'X';
const x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing size');
}
for (let i = 0; i < x; i++) {
  console.log(myVar.repeat(x));
}
