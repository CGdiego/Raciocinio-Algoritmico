numero = int(input("Digite um número inteiro: "))

if numero >= 10:
    if numero % 2 == 0:
        numero = numero * 2
    else:
        numero = numero * 3
else:
    numero = (numero + 10) * 5

print(numero)