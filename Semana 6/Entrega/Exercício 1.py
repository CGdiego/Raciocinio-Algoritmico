quant = 0

for i in range(101): # De 0 até 100
    if i % 3 == 0 and i % 5 != 0: # Verifica se i é divisível por 3 e não é divisível por 5
        print(i)
        quant += 1 # Aumenta a variável quant em +1

print(f"\n{quant} números atenderam à condição.")