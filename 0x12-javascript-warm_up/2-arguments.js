#!/usr/bin/node

const len = process.argv.length;

if (len < 3) {
  console.log('No argument');
} else if (len > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
