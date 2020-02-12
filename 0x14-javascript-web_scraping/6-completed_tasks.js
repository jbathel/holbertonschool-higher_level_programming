#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, request, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const results = {};
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed) {
        results[tasks[i].userId] += 1;
      } else {
        results[tasks[i].userId] = 0;
      }
    }
    console.log(results);
  }
});
