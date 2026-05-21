vetor = [0.0] * 10

for i in range(len(vetor)):
    vetor[i] = float(input(f"Digite o {i+1}º valor: "))

maior = vetor[0]
posicaoM = 0

for i in range(len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
        posicaoM = i

print(vetor)
print(maior)
print(posicaoM)