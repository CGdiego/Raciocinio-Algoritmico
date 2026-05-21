vetor = [0] * 6

for i in range(len(vetor)):
    vetor[i] = int(input(f"Digite o {i+1}º valor par: "))
    while vetor[i] % 2 != 0:
        vetor[i] = int(input(f"Digite o {i+1}º valor par: "))

for i in range(len(vetor)-1,-1,-1):
    print(vetor[i])