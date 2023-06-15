#!/usr/bin/node

const dict = require('./101-data').dict;
const new_dict = {};

for (const entry in dict) {
  if (!new_dict[dict[entry]]) {
    new_dict[dict[entry]] = [];
  } 
  new_dict[dict[entry]].push(entry);
}

console.log(new_dict);
