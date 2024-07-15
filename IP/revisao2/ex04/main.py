maiorData = ""

dia1, mes1, ano1 = [int(x) for x in input("Digite a primeira data: ").split("/")]
dia2, mes2, ano2 = [int(x) for x in input("Digite a segunda data: ").split("/")]

if ano1 > ano2:
    maiorData = f"{dia1:02}/{mes1:02}/{ano1}"
elif ano2 > ano1:
    maiorData = f"{dia2:02}/{mes2:02}/{ano2}"
else:
    if mes1 > mes2:
        maiorData = f"{dia1:02}/{mes1:02}/{ano1}"
    elif mes2 > mes1:
        maiorData = f"{dia2:02}/{mes2:02}/{ano2}"
    else:
        if dia1 > dia2:
            maiorData = f"{dia1:02}/{mes1:02}/{ano1}"
        elif dia2 > dia1:
            maiorData = f"{dia2:02}/{mes2:02}/{ano2}"

print(maiorData)
