valores = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(len(valores)):
    valores[i] = float(input(f"Insira o {i+1}º valor do vetor: "))

maior = valores[0]
menor = valores[0]

for valor in valores:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")