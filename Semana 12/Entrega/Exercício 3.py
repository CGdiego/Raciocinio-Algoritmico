matriz = [
    [0] * 4,
    [0] * 4,
    [0] * 4,
    [0] * 4,
    [0] * 4
]

for linha in range(5):
    for coluna in range(4):
        if coluna == 0:
            matriz[linha][coluna] = input(f"Insira o número de matrícula do {linha+1}º aluno: ")
            while not matriz[linha][coluna].isdigit():
                print("Valor inválido.\n")
                matriz[linha][coluna] = input(f"Insira o número de matrícula do {linha+1}º aluno: ")
            matriz[linha][coluna] = int(matriz[linha][coluna])
        elif coluna == 1:
            matriz[linha][coluna] = input(f"Insira a média das provas do {linha+1}º aluno: ")
            while not matriz[linha][coluna].isdigit():
                print("Valor inválido.\n")
                matriz[linha][coluna] = input(f"Insira a média das provas do {linha+1}º aluno: ")
            matriz[linha][coluna] = int(matriz[linha][coluna])
        elif coluna == 2:
            matriz[linha][coluna] = input(f"Insira a média dos trabalhos do {linha+1}º aluno: ")
            while not matriz[linha][coluna].isdigit():
                print("Valor inválido.\n")
                matriz[linha][coluna] = input(f"Insira a média dos trabalhos do {linha+1}º aluno: ")
            matriz[linha][coluna] = int(matriz[linha][coluna]) 

maior = -1
matricula = -1
matriculaM = -1

for linha in range(5):
    conta = 0
    for coluna in range(4):
        if coluna == 0:
            matricula = matriz[linha][coluna]
        elif coluna == 1 or coluna == 2:
            conta += matriz[linha][coluna]
    matriz[linha][3] = conta
    if conta > maior:
        matriculaM = matricula
        maior = conta

print(f"\nA matrícula do aluno com a maior nota final é {matriculaM}.")