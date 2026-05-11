vetor = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(len(vetor)):
    vetor[i] = float(input(f"Digite o {i+1}º valor: "))

print(f"\n{vetor}\n")

X = input("Escolha uma posição X do vetor (1-8): ")
while not X.isdigit() or int(X) > 8 or int(X) < 1:
    X = input("Escolha uma posição X do vetor (1-8): ")
X = int(X)

Y = input("Escolha uma posição Y do vetor (1-8): ")
while not Y.isdigit() or int(Y) > 8 or int(Y) < 1:
    Y = input("Escolha uma posição Y do vetor (1-8): ")
Y = int(Y)

print(f"A soma dos valores das posições X e Y é {vetor[X-1] + vetor[Y-1]}.")