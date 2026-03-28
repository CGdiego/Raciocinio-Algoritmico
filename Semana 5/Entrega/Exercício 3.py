numero = 0
media = 0
quantidade = 0

while numero != -1:
    numero = float(input("Insira um número: "))
    if numero != -1:
        quantidade += 1
        media = (numero + media)

media = media/quantidade

print("A média dos números digitados é " + str(media) + ".")