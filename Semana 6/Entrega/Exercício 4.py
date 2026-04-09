valor = int(input("Insira um valor inteiro: "))

for linha in range(valor):
    for coluna in range(valor):
        print("*", end=" ")
    print()