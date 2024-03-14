def palindrome(word: str) -> str:
    """
    Funkcja ma za zadanie odwrócić sentencję podaną przez użytkownika
    :param word: wejściowy łańcuch znaków
    :return: palindrom wejściowego łańcucha znaków
    """
    return word[::-1]


if __name__ == '__main__':
    sentencja = input('Podaj ciąg znaków: ')
    print(f"Palindrom ciągu wejściowego to: {palindrome(sentencja)}")
