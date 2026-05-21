def contar_caracteres(string, caractere):
    quant = 0
    for s in string:
        if s == caractere:
            quant += 1
    return quant

def main():
    print(contar_caracteres("paralelepípedo", "e"))

main()