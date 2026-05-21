def inverter(string):
    stringRev = ""
    stringLista = []
    stringRevLista = []

    for letra in string:
        stringLista.append(letra)

    stringRevLista = reversed(stringLista)

    for letra in stringRevLista:
        stringRev += letra

    return stringRev

print(inverter("Diego"))