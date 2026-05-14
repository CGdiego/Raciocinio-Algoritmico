matriz = [
    [0] * 5,
    [0] * 5,
    [0] * 5,
    [0] * 5,
    [0] * 5,
]

for linha in range(5):
    for coluna in range(5):
        if linha == coluna:
            matriz[linha][coluna] = 1
        else:
            matriz[linha][coluna] = 0