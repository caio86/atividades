function show(empresas) {
  let biggerNameSize = 0;

  for (const empresa of empresas) {
    if (biggerNameSize < empresa.name.length) {
      biggerNameSize = empresa.name.length;
    }
  }

  let result = Array.from(empresas)
    .map((empresa) => {
      return (
        empresa.name.padEnd(biggerNameSize, ".") +
        "..." +
        empresa.founded +
        "..." +
        empresa.industry.join("<>")
      );
    })
    .join("\n");

  return result;
}

const companies = [
  { name: "Amazon", founded: 1994, industry: ["E-commerce", "Cloud"] },
  { name: "Facebook", founded: 2004, industry: ["Social"] },
  {
    name: "Alphabet Inc.",
    founded: 2015,
    industry: ["Search", "Cloud", "Advertising"],
  },
];

companies.map((empresa) => (empresa.kind = "Internet company"));

console.log(show(companies));
