lado1 = float(input("Insira o tamanho do primeiro lado do triângulo: "))
lado2 = float(input("Insira o tamanho do segundo lado do triângulo: "))
lado3 = float(input("Insira o tamanho do terceiro lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    triangulo = True
else:
    triangulo = False
    print("Isso não é um triângulo.")

if triangulo:
    if lado1 == lado2 == lado3:
        print("É um triângulo equilátero.")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("É um triângulo escaleno.")
    else:
        print("É um triângulo isósceles.")

    if lado1 > lado2 and lado1 > lado3:
        if lado1**2 == lado2**2 + lado3**2:
            print("Este triângulo é retângulo.")
        else:
            print("Este triângulo não é retângulo.")
    elif lado2 > lado1 and lado2 > lado3:
        if lado2**2 == lado1**2 + lado3**2:
            print("Este triângulo é retângulo.")
        else:
            print("Este triângulo não é retângulo.")
    elif lado3 > lado1 and lado3 > lado2:
        if lado3**2 == lado1**2 + lado2**2:
            print("Este triângulo é retângulo.")
        else:
            print("Este triângulo não é retângulo.")
    else:
        print("Este triângulo não é retângulo.")
