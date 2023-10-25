#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const fPath = process.argv[3];

request(URL, (error, response, body) => {
  if (!error) {
    fs.writeFile(fPath, body, 'utf-8', err => {
      if (err) console.error(err);
    });
  }
});
