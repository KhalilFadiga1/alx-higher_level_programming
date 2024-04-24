#!/usr/bin/node

const argTwo = process.argv[2];
const changeStr = parseInt(argTwo);

if (isNaN(argTwo)) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  while (i < changeStr) {
    console.log('C is fun');
    i++;
  }
}
