function max(list) {
  let min = list[0];
  for (let valor of list) {
    if (valor < min) {
      min = valor;
    }
  }
  return min;
}

function max(list) {
  let max = list[0];
  for (let valor of list) {
    if (valor > max) {
      max = valor;
    }
  }
  return max;
}

function range(start, stop, step = 1) {
  let list = [];

  if (start < stop) {
    for (let x = start; x < stop; x += step) {
      list.push(x);
    }
  }

  if (start > stop) {
    for (let x = start; x > stop; x -= step) {
      list.push(x);
    }
  }

  return list;
}

function uniq(list) {
  let uniq = [];

  for (let valor of list) {
    if (!uniq.includes(valor)) {
      uniq.push(valor);
    }
  }

  return uniq;
}

function sortNum(list) {
  return list.sort((a, b) => a - b);
}

function zip(...lists) {
  let resultado = [];

  for (let i = 0; i < lists[0].length; i++) {
    tmp = [];
    for (let x = 0; x < lists.length; x++) {
      tmp.push(lists[x][i]);
    }
    resultado.push(tmp);
  }

  return [...resultado];
}

console.log(zip(["moe", "larry"], [30, 40]));
