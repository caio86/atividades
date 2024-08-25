function min(list) {
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

  if (stop == undefined) {
    stop = start;
    start = 0;
  }

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

  return sortNum(uniq);
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

console.log(min([1, 4, 2, 6, 10, 3]));
console.log(min([1, 4, -1, 6, 10, 3]));
console.log(max([1, 4, 2, 6, 10, 3]));
console.log(range(10));
console.log(range(1, 11));
console.log(range(0, 30, 5));
console.log(zip(["moe", "larry"], [30, 40]));
console.log(zip(["moe", "larry", "curly"], [30, 40, 50], [true, false, false]));
console.log(uniq([1, 2, 1, 4, 1, 3]));
console.log(uniq([1, 2, 1, 3, 3]));
console.log(sortNum([1, 3, 2]));
console.log(sortNum([1, 2, 10, 3, 32]));
