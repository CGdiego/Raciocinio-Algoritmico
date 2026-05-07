numero = int(input("Digite um número inteiro: "))
resultado = 0

if numero >= 10:
    if numero % 2 == 0:
        resultado = numero * 2
    else:
        resultado = numero * 3
else:
    resultado = (numero + 10) * 5

print(resultado)