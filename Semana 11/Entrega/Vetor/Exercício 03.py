conjunto1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
conjunto2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(len(conjunto1)):
    conjunto1[i] = float(input(f"Insira o {i+1}º valor real: "))

for i in range(len(conjunto1)):
    conjunto2[i] = conjunto1[i]**2

print(f"\n{conjunto1}")
print(f"{conjunto2}\n")