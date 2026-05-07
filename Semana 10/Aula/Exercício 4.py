numeros = [5, 7, 12, 2, 9, 21]
i = 0

while i < 6:
    print(numeros[i] * 2)
    i += 1

for i in range(len(numeros)):
    print(numeros[i] * 2)

for numero in numeros:
    print(numero * 2)
    numero += 1