#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

function groupByValue(inputObj) {
	for (let key of Object.keys(dict)) {
		const value = inputObj[key];
		if (newDict[value] === undefined) {
			newDict[value] = [];
		}
		newDict[value].push(key);
	}
	return newDict;
}

console.log(groupByValue(dict));
