#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const done = {};
    const notDone = JSON.parse(body);
    notDone.forEach((todo) => {
      if (todo.completed && done[todo.userId] === undefined) {
        done[todo.userId] = 1;
      } else if (todo.completed) {
        done[todo.userId] += 1;
      }
    });

    console.log(done);
  }
});
