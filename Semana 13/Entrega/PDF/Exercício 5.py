def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def main():
    while True:
        escolha = input("Escolha uma das opções seguintes:\n[0] - Sair\n[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n")
        while escolha not in ["0", "1", "2", "3", "4"]:
            print("Opção inválida.\n")
            escolha = input("Escolha uma das opções seguintes:\n[0] - Sair\n[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n")

        if escolha == "0":
            exit()

        x = float(input("\nDigite um valor X: "))
        y = float(input("\nDigite um valor Y: "))

        if escolha == "1":
            print(soma(x, y))
        elif escolha == "2":
            print(subtracao(x, y))
        elif escolha == "3":
            print(multiplicacao(x, y))
        else:
            print(divisao(x, y))

main()