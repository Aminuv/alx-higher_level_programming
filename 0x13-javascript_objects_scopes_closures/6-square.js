#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      let r = '';
      for (let y = 0; y < this.width; y++) {
        r += c;
      }
      console.log(r);
    }
  }
}

module.exports = Square;
