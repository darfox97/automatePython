""" Exercise 7 """


def es_palindromo(texto):
    """ Function to set if a text is palindrome or not. """

    texto_minusculas = texto.strip().lower()
    texto_minusculas = texto_minusculas.replace(" ", "")

    lst = []
    for char in texto_minusculas:
        lst.append(char)

    print(lst)

    rvrslst = []
    for char in texto_minusculas:
        rvrslst.insert(0, char)

    print(rvrslst)
    if lst == rvrslst:
        return True
    else:
        return False


print(es_palindromo("Hola Mundo"))
print(es_palindromo("Abba"))
