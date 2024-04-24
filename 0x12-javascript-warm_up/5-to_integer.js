#!/usr/bin/node

const argTwo = process.argv[2];
const changeNum = parseInt(argTwo);

if (isNaN(changeNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${changeNum}`);
}
