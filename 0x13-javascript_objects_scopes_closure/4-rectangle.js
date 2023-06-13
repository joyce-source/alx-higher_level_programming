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

  rotate () {
    if (!this.width || !this.height) {
      console.log('Empty rectangle');
      return;
    }

    [this.width, this.height] = [this.height, this.width];
    console.log('Rectangle rotated');
  }

  double () {
    if (!this.width || !this.height) {
      console.log('Empty rectangle');
      return;
    }

    this.width *= 2;
    this.height *= 2;
    console.log('Rectangle dimensions doubled');
  }
}

module.exports = Rectangle;
