valores = [0, 0, 0, 0, 0, 0]

for i in range(len(valores)):
    valores[i] = input(f"Insira o {i+1}º valor inteiro: ")
    while not valores[i].lstrip('-').isdigit(): # Verifica se é inteiro, o 'lstrip' está ali porque o 'isdigit' não deixa colocar negativos
        valores[i] = input(f"Insira o {i+1}º valor inteiro: ")
    valores[i] = int(valores[i])

print(f"\n{valores}\n")
for valor in valores:
    print(valor)