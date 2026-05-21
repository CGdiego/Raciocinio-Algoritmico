def soma_elementos(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

def main():
    print(soma_elementos([1, 3, 5, 2, 4]))

main()