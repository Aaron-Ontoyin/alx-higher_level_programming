#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);
request(url, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;

    characters.forEach((character) => {
      request(character, function (err, response, body) {
        if (!err) {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    });
  }
});
