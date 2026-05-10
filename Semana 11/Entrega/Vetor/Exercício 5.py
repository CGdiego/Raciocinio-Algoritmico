valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
par = 0

for i in range(len(valores)):
    valores[i] = input(f"Insira o seu {i+1}º valor inteiro: ")
    while not valores[i].isdigit():
        valores[i] = input(f"Insira o seu {i+1}º valor inteiro: ")
    valores[i] = int(valores[i])
    
    if valores[i] % 2 == 0:
        par += 1

print(f"O vetor digitado possui {par} valores pares.")    