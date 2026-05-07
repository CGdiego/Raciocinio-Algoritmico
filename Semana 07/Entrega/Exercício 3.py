n1 = int(input("Insira um número inicial: "))
n2 = int(input("Insira um número final: "))

for i in range(n1,n2+1): # Seleciona os números da tabuada
    print(f"Tabuada do {i}:") # Só pra deixar mais ajeitado com o título
    for tabuada in range(1, 11): # Vai de 1 até 10
        print(i * tabuada) # Multiplica o número da tabuada pelo multiplicador
    print() # Separa as linhas