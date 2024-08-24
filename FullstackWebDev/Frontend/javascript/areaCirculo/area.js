function calculaAreaCirculo(raio) {
  return Math.PI * raio ** 2;
}

function main() {
  let input = require("fs").readFileSync("./areaCirculoInput", "utf-8");
  let lines = input.split("\n");
  lines.pop();

  for (let line of lines) {
    raio = Number(line);
    console.log(calculaAreaCirculo(raio));
  }
}

main();
