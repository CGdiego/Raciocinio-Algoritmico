# Ainda não terminei :/
i = ()

while not i:
    expressao = input("Insira a expressão matemática (ou digite 'Sair' para sair): ").lower()

    if expressao == "sair":
        break

    partes = expressao.split()

    no1 = float(partes[0])
    operacao = partes[1]
    no2 = float(partes[2])

    while operacao not in ["+", "-", "*", "/", "%"]:
        operacao = input("Insira um operador válido: ")

    if operacao == "+":
        print(no1 + no2)
    elif operacao == "-":
        print(no1 - no2)
    elif operacao == "*":
        print(no1 * no2)
    elif operacao == "/":
        print(no1 / no2)
    else:
        print(no1 % no2)