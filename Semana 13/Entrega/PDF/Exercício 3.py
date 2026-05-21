def maior_elemento(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

def main():
    print(maior_elemento([12, 90, -10, -1923, 0]))

main()