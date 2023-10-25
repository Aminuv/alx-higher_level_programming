#!/usr/bin/node
//prints all characters of a Star Wars movie.
const request = require('request');
const id = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(URL, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    for (const charURL of characters) {
      request(charURL, (error, response, body) => {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
