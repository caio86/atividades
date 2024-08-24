function calculadora(operador, num1, num2) {
  switch (operador) {
    case "+":
      return num1 + num2;
    case "-":
      return num1 - num2;
    case "*":
      return num1 * num2;
    case "/":
      return num1 / num2;
    default:
      return "Invalid operator";
  }
}

let input = require("fs").readFileSync("./calculadora_input", "utf-8");
let lines = input.split("\n");
lines.pop();

for (let line of lines) {
  let values = line.split(", ");
  let numbers = values.slice(0, 2);
  numbers = numbers.map((x) => Number(x));

  resultado = calculadora(values[2], numbers[0], numbers[1]);
  console.log(resultado);
}
