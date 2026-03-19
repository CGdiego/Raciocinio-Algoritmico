ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and not ano % 100 == 0) or ano % 400 == 0:
    print(str(ano) + " é bissexto.")
else:
    print(str(ano) + " não é bissexto.")