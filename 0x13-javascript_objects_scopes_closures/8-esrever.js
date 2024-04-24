#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  let x = 0;
  while ((len - 1) > 0) {
    const aux = list[len];
    list[len] = list[x];
    list[x] = aux;
    x++;
    len--;
  }
  return list;
};
