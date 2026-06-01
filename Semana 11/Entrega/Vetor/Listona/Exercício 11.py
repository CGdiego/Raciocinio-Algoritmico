vetor = [0.0] * 10
negativos = 0
somaPos = 0

for i in range(len(vetor)):
    vetor[i] = float(input(f"Insira o {i+1}º número real: "))
    if vetor[i] < 0:
        negativos += 1
    else:
        somaPos += vetor[i]

print(negativos)
print(somaPos)