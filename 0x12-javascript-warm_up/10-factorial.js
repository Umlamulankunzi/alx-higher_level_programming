#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) { return (1); }
  if (n <= 1) { return (n); }
  return n * factorial(n - 1);
}

console.log(factorial(Number(process.argv[2])));
