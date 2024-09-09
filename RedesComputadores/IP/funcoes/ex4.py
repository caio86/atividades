def fatorial(n: int):
    if n <= 1:
        return 1

    return n * fatorial(n - 1)


def main():
    print(fatorial(5))
    print(fatorial(4))
    print(fatorial(6))
    print(fatorial(10))


main()
