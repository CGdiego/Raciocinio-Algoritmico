i = 0
numero = 0
par = 0
impar = 0

while i < 10:
    numero = float(input("Insira um número: "))
    i += 1
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Você digitou {par} número(s) pares.")
print(f"Você digitou {impar} número(s) ímpares.")