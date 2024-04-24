#!/usr/bin/node

const argList = process.argv.slice(2);
const nums = argList.map(arg => parseInt(arg));
const sortedValues = nums.sort((x, y) => y - x);

if (nums.length < 2) {
  console.log(0);
} else {
  console.log(sortedValues[1]);
}
