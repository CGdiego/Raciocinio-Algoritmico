valores = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
negativo = 0
somaPos = 0

for i in range(len(valores)):
    valores[i] = float(input(f"Digite o {i+1}º valor real: "))

    if valores[i] < 0:
        negativo += 1

    if valores[i] > 0:
        somaPos += valores[i]

print(f"\nForam digitados {negativo} números negativos e a soma dos números positivos resulta em {somaPos}.")