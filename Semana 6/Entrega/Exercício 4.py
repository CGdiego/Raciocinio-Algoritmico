valor = int(input("Insira um valor inteiro: "))

for linha in range(1,valor+1):
    for coluna in range(1,linha+1):
        print(coluna, end=" ")
    print()