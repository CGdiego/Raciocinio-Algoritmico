vetor = [0, 0, 0, 0, 0, 0]
sena = [9, 13, 21, 32, 33, 59] # Valores da última Mega da Virada
acertos = 0

for i in range(6):
    aposta = input(f"Insira o seu {i+1}º número para a Mega-Sena: ")

    # Enquanto não for número
    while not aposta.isdigit() or int(aposta) > 60 or int(aposta) < 1 or int(aposta) in vetor:
        print("\nValor inválido, digite novamente.")
        aposta = input(f"Insira o seu {i+1}º número para a Mega-Sena: ")

    aposta = int(aposta)
    vetor[i] = aposta

    for s in sena:
        if vetor[i] == s:
            acertos += 1

print(f"\nNúmeros sorteados: {sena}.")
print(f"Números jogados: {vetor}.")
print(f"Quantidade de acertos: {acertos}/6.")