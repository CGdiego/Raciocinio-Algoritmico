vetor = [0.0] * 10
vetorSqrt = [0.0] * 10

for i in range(len(vetor)):
    vetor[i] = float(input(f"Insira o {i+1}º valor: "))
    vetorSqrt[i] = vetor[i]**2

print(vetor)
print(vetorSqrt)