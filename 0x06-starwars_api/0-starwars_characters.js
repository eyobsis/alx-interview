#!/usr/bin/node

const request = require('request');

if (process.argv.length!== 3) {
  console.error('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        process.exit(1);
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
