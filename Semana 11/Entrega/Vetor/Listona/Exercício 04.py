valores = [0] * 8
X = -1
Y = -1

for i in range(len(valores)):
    valores[i] = float(input(f"Insira o {i+1}º valor: "))

while X > 7 or X < 0:
    X = int(input("Insira uma posição X do vetor: "))

while Y > 7 or Y < 0:
    Y = int(input("Insira uma posição Y do vetor: "))

soma = valores[X] + valores[Y]
print(soma)