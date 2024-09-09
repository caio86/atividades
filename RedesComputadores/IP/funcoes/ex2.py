def print_e(text: str, n: int):
    for symbol in text:
        print(symbol, end=" " * n)

    print()


def main():
    print_e("teste", 5)
    print_e("cavalo", 2)
    print_e("casa", 10)


main()
