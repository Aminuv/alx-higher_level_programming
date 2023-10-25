#!/usr/bin/node
// matches a given integer.
const request = require('request');
const idu = process.argv[2];
const URL = 'https://swapi-api.alx-tools.com/api/films/' + idu;
request(URL, (error, response, body) => {
  if (error) console.log(error);
  const data = JSON.parse(body);
  console.log(data.title);
});
