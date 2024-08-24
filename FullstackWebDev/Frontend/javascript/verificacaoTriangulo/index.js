function getInput() {
  let input = require("fs").readFileSync("./input", "utf-8");
  let lines = input.split("\n");
  lines.pop();
  return lines.map((x) => x.split(", "));
}

const isTriangle = (lados) => {
  if (
    lados[0] >= lados[1] + lados[2] ||
    lados[1] >= lados[2] + lados[0] ||
    lados[2] >= lados[0] + lados[1]
  ) {
    return false;
  }
  return true;
};

function getTriangleType(side1, side2, side3) {
  if (!isTriangle([side1, side2, side3])) {
    return "none";
  }
  if (side1 == side2 && side1 == side3) {
    return "equilateral";
  }
  if (side1 != side2 && side1 != side3 && side2 != side3) {
    return "scalene";
  }
  return "isosceles";
}

function main() {
  input = getInput();
  input = input.map((x) => x.map(Number));
  for (let line of input) {
    console.log(getTriangleType(...line));
  }
}

main();
