const body = document.body;

/**
 * @param {string} cep
 * @returns {object}
 * */
async function searchCEP(cep) {
  if (cep.length == 0) {
    return { erro: "CEP não informado!" };
  }
  const URL = `https://viacep.com.br/ws/${cep}/json/`;
  const data = await fetch(URL)
    .then((res) => res.json())
    .catch(() => {
      return { erro: "true" };
    });

  return data;
}

function limparForm(form) {
  form["rua"].value = "";
  form["bairro"].value = "";
  form["estado"].value = "";
  form["cidade"].value = "";
}

async function autoCompleteForm() {
  const form = document.forms["cadastroEndereco"];
  const errorCEP = document.getElementById("error-cep");

  errorCEP.classList = "oculto";
  let cpf = form["cep"].value;

  const data = await searchCEP(cpf);
  console.log(data);
  if (data.erro == "true") {
    errorCEP.classList = "";
    limparForm(form);
    return;
  }

  if (data.erro == "CEP não informado!") {
    console.log("haha");
    limparForm(form);
    return;
  }

  form["rua"].value = data.logradouro;
  form["bairro"].value = data.bairro;
  form["estado"].value = data.uf;
  form["cidade"].value = data.localidade;
}
