i = ()

while not i:
    operacao = input("Insira a expressão matemática, ou digite 'Sair' para sair: ").lower()
    if operacao == "sair":
        break
    operacao = eval(operacao)
    print(f"O resultado da operação é {operacao}.")