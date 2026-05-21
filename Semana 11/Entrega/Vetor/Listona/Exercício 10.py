vetor = [0.0] * 15
media = 0

for i in range(len(vetor)):
    vetor[i] = int(input(f"Digite o valor da nota do {i+1}º aluno (0-10): "))
    while vetor[i] > 10 or vetor[i] < 0:
        vetor[i] = int(input(f"Digite o valor da nota do {i+1}º aluno (0-10): "))
    media += vetor[i]

media /= len(vetor)

print(media)