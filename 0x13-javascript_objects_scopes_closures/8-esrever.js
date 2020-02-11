#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  const length = list.length - 1;

  for (let i = length; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};
