QTD_ALUNOS = 20

alunos: list[list[int]] = []
mediaAlunos: list[float] = []
mediaTurma = 0
maiorNota = 0
qtdAcimaDaMedia = 0

for i in range(QTD_ALUNOS):
    notas = [0] * 3
    notas[0] = int(input(f"Nota 1 do {i+1}° aluno: "))
    notas[1] = int(input(f"Nota 2 do {i+1}° aluno: "))
    notas[2] = int(input(f"Nota 3 do {i+1}° aluno: "))

    maiorNota = max(maiorNota, max(notas))
    alunos.append(notas)
    mediaAlunos.append(sum(notas) / len(notas))

mediaTurma = sum(mediaAlunos) / QTD_ALUNOS

for i, media in enumerate(mediaAlunos, 1):
    print(f"Media do aluno {i}: {media:.2f}")
    if media > mediaTurma:
        qtdAcimaDaMedia += 1

print("Maior nota:", maiorNota)
print(f"{qtdAcimaDaMedia} alunos ficaram acima da media.")
