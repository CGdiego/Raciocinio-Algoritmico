valores = [0.0, 0.0, 0.0, 0.0, 0.0]
media = 0

for i in range(len(valores)):
    valores[i] = float(input(f"Digite o {i+1}º valor: "))
    media += valores[i]

media /= len(valores)

maior = valores[0]
menor = valores[0]

for valor in valores:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"O maior valor foi {maior}, o menor valor foi {menor} e a média foi {media}.")