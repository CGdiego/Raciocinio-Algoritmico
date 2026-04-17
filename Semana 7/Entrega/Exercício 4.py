valor = int(input("Insira um valor inteiro: "))

for linha in range(1,valor+1): # Esse loop controla quantas linhas vão aparecer
    for coluna in range(1,linha+1): # Imprime números de 1 até o número da linha atual
        print(coluna, end=" ") # Imprime na linha com espaço
    print() # Depois que termina a linha, ele pula pra próxima