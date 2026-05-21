vetor = [0.0] * 10

for i in range(len(vetor)):
    vetor[i] = float(input(f"Digite o {i+1}º valor: "))

maior = vetor[0]
menor = vetor[0]

for v in vetor:
    if v > maior:
        maior = v
    if v < menor:
        menor = v

print(maior)
print(menor)