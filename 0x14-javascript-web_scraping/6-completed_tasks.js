#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
const dic = {};

request(URL, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    for (const task of todos) {
      if (task.completed && !(task.userId in dic)) {
        dic[task.userId] = 0;
      }
      if (task.completed) {
        dic[task.userId] += 1;
      }
    }
    console.log(dic);
  }
});
