#!/usr/bin/node
function add(a, b) {
  const result = a + b;
  console.log(result);
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

add(arg1, arg2);
