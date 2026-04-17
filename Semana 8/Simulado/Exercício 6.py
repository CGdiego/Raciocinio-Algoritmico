num = int(input("Digite um número para calcular o fatorial: "))
resultado = num
i = num - 1

while i > 0:
    resultado = resultado * i
    i -= 1

print("O fatorial de" + str(num) + "é" + str(resultado))