#!/usr/bin/node

const supSquare = require('./5-square');

class Square extends supSquare {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let x = 0; x < this.width; x++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
