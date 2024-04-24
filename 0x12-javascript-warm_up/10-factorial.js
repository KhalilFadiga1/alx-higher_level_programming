#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}

const argTwo = parseInt(process.argv[2]);
const res = factorial(argTwo);

console.log(res);
