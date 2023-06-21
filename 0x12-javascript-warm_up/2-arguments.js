#!/usr/bin/node
/*
This script prints a message depending on the number of arguments passed.
*/

const args = process.argv.slice(2);
const numArgs = args.length;

if (numArgs === 0) {
  console.log("No argument");
} else if (numArgs === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
