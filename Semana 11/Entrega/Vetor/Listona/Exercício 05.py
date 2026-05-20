vetor = [0] * 10
par = 0

for i in range(len(vetor)):
    vetor[i] = int(input(f"Insira o {i+1}º valor: "))

for v in vetor:
    if v % 2 == 0:
        par += 1

print(f"O vetor possui {par} valores pares.")