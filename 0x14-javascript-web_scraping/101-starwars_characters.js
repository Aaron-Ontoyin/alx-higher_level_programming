#!/usr/bin/node

const request = require('request');

function getFilmCharacters(filmId) {
  const url = `https://swapi.co/api/films/${filmId}`;
  request(url, function (error, response, body) {
    if (error) {
      console.error('Error fetching film:', error);
    } else {
      const characters = JSON.parse(body).characters;
      printCharacters(characters, 0);
    }
  });
}

function printCharacters(characters, index) {
  if (index >= characters.length) return;

  request(characters[index], function (error, response, body) {
    if (error) {
      console.error('Error fetching character:', error);
    } else {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <filmId>');
  process.exit(1);
}

const filmId = process.argv[2];
getFilmCharacters(filmId);
