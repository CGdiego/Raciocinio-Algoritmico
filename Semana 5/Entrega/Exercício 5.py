import time # Importar timer
i = ()

while not i: # Loop infinito
    print("Escolha um operação:")
    print("1: Soma")
    print("2: Substração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    escolha = int(input("\n"))
    if escolha == 0: # Sair
        break
    if escolha >= 1 and escolha <= 4: # Opções válidas
        n1 = float(input("\nInforme o primeiro número: "))
        n2 = float(input("\nInforme o segundo número: "))
        if escolha == 4 and n2 == 0: #Se estiver dividindo por 0, tentar novamente
            while n2 == 0:
                n2 = float(input("\nInforme um segundo valor diferente de zero: "))
        if escolha == 1:
            print(f"\nO resultado da operação é {n1 + n2}.\n")
        elif escolha == 2:
            print(f"\nO resultado da operação é {n1 - n2}.\n")
        elif escolha == 3:
            print(f"\nO resultado da operação é {n1 * n2}.\n")
        else:
            print(f"\nO resultado da operação é {n1 / n2}.\n")
        time.sleep(3) # Esperar 3 segundos
    else:
        print("Insira uma opção válida.\n") # Usuário colocou uma opção inválida