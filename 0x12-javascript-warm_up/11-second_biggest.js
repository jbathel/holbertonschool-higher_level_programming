#!/usr/bin/node

let array = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  array = (process.argv.slice(2));
  const secondLargest = array.sort(function (a, b) { return a - b; })[array.length - 2];
  console.log(secondLargest);
}
