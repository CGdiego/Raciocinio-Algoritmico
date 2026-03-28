# Variáveis
valor = int(input("Insira um valor inteiro:\n"))
i = valor
plus = 0
conta = 0

print("\n")

# Loop
while i > 0:
    conta = (valor - 1 * plus) + conta
    i -= 1
    plus += 1

print (conta)