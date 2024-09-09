def soma(n: list[int]):
    nSoma = 0
    for num in n:
        nSoma += num

    return nSoma


def main():
    print(soma([1, 2, 3]))
    print(soma([5, 4, 10]))
    print(soma([10, 100, 1000]))


main()
