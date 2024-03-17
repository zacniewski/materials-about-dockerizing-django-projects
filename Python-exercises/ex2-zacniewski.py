def replacer(wej: str) -> str:
    """
    Cel funkcji to zamienić wszystkie litery 'o' na 0, 'e' na 3, 'i' na 1, 'a' na 4
    w podanej przez użytkownika sentencji.
    :param wej: ciąg wejściowy znaków
    :return: ciąg po zamianie wybranych elementów
    """
    return (wej.replace('o', '0').replace('e', '3').
            replace('i', '1').replace('a', '4'))


if __name__ == '__main__':
    wejscie = input('Podaj ciąg znaków: ')
    print(f"Zmieniony ciąg to: {replacer(wejscie)}")
