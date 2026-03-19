peso = float(input("Insira seu peso em quilos: "))
altura = float(input("Insira sua altura em metros: "))

imc = (peso / (altura**2))

print("O seu IMC é " + str(imc))