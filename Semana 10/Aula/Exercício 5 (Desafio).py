vetor = [0, 0, 0, 0, 0, 0]

for i in range(6):
    aposta = input(f"Insira o seu {i+1}º número para a Mega-Sena: ")

    # Enquanto não for número
    while not aposta.isdigit():
        aposta = input(f"Insira o seu {i+1}º número para a Mega-Sena: ")

    aposta = int(aposta)

    vetor[i] = aposta

print(vetor)