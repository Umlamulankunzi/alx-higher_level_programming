#!/usr/bin/node
const x = process.argv[2];

if (parseInt(x)) {
  for (let count = 0; count < x; count++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
