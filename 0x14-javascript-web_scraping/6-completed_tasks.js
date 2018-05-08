#!/usr/bin/node
let request = require('request');
let tasks = {};
request(process.argv[2], (err, res, body) => {
  if (err) throw err;
  let data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    let uid = data[i].userId;
    if (data[i].completed === true) {
      if (!(uid in tasks)) {
        tasks[uid] = 1;
      } else {
        tasks[uid] += 1;
      }
    }
  }
  console.log(tasks);
});
