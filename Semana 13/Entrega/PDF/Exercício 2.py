def e_palindromo(string):
    stringRev = ""
    stringLista = []
    stringRevLista = []

    for letra in string:
        stringLista.append(letra)

    stringRevLista = reversed(stringLista)

    for letra in stringRevLista:
        stringRev += letra

    if string.lower() == stringRev.lower():
        return True
    else:
        return False
    
def main():
    print(e_palindromo("Arara"))

main()