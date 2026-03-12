anoAtual = int(input("Insira o ano atual: "))
ano = int(input("Insira seu ano de nascimento: "))

idade1 = ((anoAtual-1) - ano)
idade2 = (anoAtual - ano)

print("Sua idade é " + str(idade1) + " ou " + str(idade2) + " anos.")