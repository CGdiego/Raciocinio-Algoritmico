anos = int(input("Insira sua idade em anos: "))
mesesAniversario = int(input("Insira quantos meses faltam para o seu aniversário: "))

meses = int(anos * 12)
mesesPassados = 12 - mesesAniversario

resultado = (meses + mesesPassados)

print("Sua idade em meses é " + str(resultado) + ".")