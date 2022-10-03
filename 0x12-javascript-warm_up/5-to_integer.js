#!/usr/bin/node
const process = require('process');
const integer = parseInt(process.argv[2]);
if (integer) {
  console.log('My number: ' + integer);
} else {
  console.log('Not a number');
}
