matrizA = [[0] * 4 for _ in range(2)]
matrizB = [[0] * 4 for _ in range(2)]
matrizC = [[0] * 4 for _ in range(2)]

for i in range(2):
    for j in range(4):
        matrizA[i][j] = int(input(f"Matriz A [{i}][{j}]: "))

for i in range(2):
    for j in range(4):
        matrizB[i][j] = int(input(f"Matriz B [{i}][{j}]: "))


for i in range(2):
    for j in range(4):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

for i in range(2):
    print(matrizC[i])
