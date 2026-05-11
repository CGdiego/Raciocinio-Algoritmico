valores = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(len(valores)):
    valores[i] = input(f"Insira o {i+1}º valor inteiro do vetor: ")
    while not valores[i].isdigit():
        valores[i] = input(f"Insira o {i+1}º valor inteiro do vetor: ")
    valores[i] = int(valores[i])

maior = valores[0]
posicao = 0

for i in range(len(valores)):
    if valores[i] > maior:
        maior = valores[i]
        posicao = i

print(f"\n{valores}")
print(f"O maior valor é {maior} e sua posição é {posicao}.")