contador = 1
numero = int(input("Insira um número:\n"))

while numero < 1 or numero > 10:
    print("O valor deve estar entre 1 e 10.")
    numero = int(input("Valor válido:\n"))

contador = 2
while contador <= 10:
    print(numero * contador)
    contador = contador + 1