notas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
media = 0

for i in range(len(notas)):
    notas[i] = float(input(f"Insira a nota do {i+1}º estudante: "))
    media += notas[i]

media /= len(notas)

print(f"\nA média de todas as notas da sala foi {media}.")