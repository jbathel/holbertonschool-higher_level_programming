#!/usr/bin/node

const originalSquare = require('./5-square');

class Square extends originalSquare {
  }

Square.prototype.charPrint = function (c) {
  if (!c) {
    c = 'X';
  }
  for (let i = 0; i < this.height; i++) {
    console.log(c.repeat(this.width));
  }
};

module.exports = Square;
