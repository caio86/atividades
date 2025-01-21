def palindrome(text: str) -> bool:
    for i in range(0, len(text) // 2):
        if text[i].lower() != text[len(text) - i - 1].lower():
            return False

    return True


def main():
    words = [
        "ovo",
        "arara",
        "casa",
        "reler",
    ]

    for word in words:
        if palindrome(word):
            print(f"A palavra {word} é um palíndromo")
        else:
            print(f"A palavra {word} não é um palíndromo")


main()
