matriz = [
    [0] * 4,
    [0] * 4,
    [0] * 4,
    [0] * 4
]

for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = input(f"Digite o número da {linha+1}ª linha e a {coluna+1}ª coluna: ")
        while not matriz[linha][coluna].lstrip('-').isdigit():
            print("Valor inválido.\n")
            matriz[linha][coluna] = input(f"Digite o número da {linha+1}ª linha e a {coluna+1}ª coluna: ")
        matriz[linha][coluna] = int(matriz[linha][coluna])

print()

for linha in range(4):
    print(matriz[linha])

maior = [0][0]

for linha in range(4):
    for coluna in range(4):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]

print()

print(f"O maior número é {maior}.")