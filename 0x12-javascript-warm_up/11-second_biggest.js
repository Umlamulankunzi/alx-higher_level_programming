#!/usr/bin/node
const args = process.argv.slice(2).map(Number).sort((a, b) => a - b);
console.log(args[args.length - 2]);
