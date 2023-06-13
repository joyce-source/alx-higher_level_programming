#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // Create an empty object if width or height is 0 or not a positive int
      return {};
    }

    this.width = w;
    this.height = h;
  }

  print () {
    if (!this.width || !this.height) {
      console.log('Empty rectangle');
      return;
    }

    const row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
