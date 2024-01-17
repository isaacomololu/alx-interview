#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as  list in the /films/ endpoint
 */

const request = require('request');

const filmNum = process.argv[2] + '/';
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + filmNum, async (err, res, data) => {
  if (err) return console.error('Error:', err);

  // find URLs of each character in the film as a list obj
  const characters = JSON.parse(data).characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, data) => {
        if (err) return console.error('Error:', err);

        // print each character name and prints in URL order
        console.log(JSON.parse(data).name);
        resolve();
      });
    });
  }
});
