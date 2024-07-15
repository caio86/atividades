QTD_LEITURAS = 20

maiorData = "00/00/00"

for _ in range(QTD_LEITURAS):
    dia, mes, ano = [int(x) for x in input("Digite uma data (dd/mm/aaaa): ").split("/")]
    maiorDia, maiorMes, maiorAno = [int(x) for x in maiorData.split("/")]

    if ano > maiorAno:
        maiorData = f"{dia:02}/{mes:02}/{ano}"
    elif ano == maiorAno:
        if mes > maiorMes:
            maiorData = f"{dia:02}/{mes:02}/{ano}"
        elif mes == maiorMes:
            if dia > maiorDia:
                maiorData = f"{dia:02}/{mes:02}/{ano}"

print(f"A maior data é: {maiorData}")
