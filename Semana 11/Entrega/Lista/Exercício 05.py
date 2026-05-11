lista = []

for i in range(5):
    lista.append(input(f"Digite a {i+1}ª palavra: "))

maior = lista[0]
menor = lista[0]

for l in lista:
    if len(l) > len(maior): # Verifique se tal elemento é maior
        maior = l
    if len(l) < len(menor): # Verifique se tal elemento é menor
        menor = l

print(f"A palavra mais longa é {maior} e a mais curta é {menor}.")