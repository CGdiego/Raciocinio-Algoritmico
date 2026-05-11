valores = [0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(len(valores)):
    valores[i] = float(input(f"Digite o {i+1}º valor: "))

maior = valores[0]
menor = valores[0]
posicaoM = 0
posicaom = 0

for i in range(len(valores)):
    if valores[i] > maior:
        maior = valores[i]
        posicaoM = i
    if valores[i] < menor:
        menor = valores[i]
        posicaom = i

print(f"A posição do maior valor é {posicaoM} e a do menor valor é {posicaom}.")