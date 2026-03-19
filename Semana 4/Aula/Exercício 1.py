temperatura = float(input("Insira a temperatura em graus Celsius: "))

if temperatura > 25:
    print("Está quente.")
elif 24 >= temperatura and temperatura >= 18:
    print("Está ameno.")
else:
    print("Está frio.")