#!/usr/bin/node

const argTwo = process.argv[2];
const changeStr = parseInt(argTwo);

if (isNaN(argTwo)) {
  console.log('Missing size');
} else {
  let i;
  const alphabet = 'X';
  for (i = 0; i < changeStr; i++) {
    console.log(alphabet.repeat(changeStr));
  }
}
