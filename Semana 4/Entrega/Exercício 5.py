x = float(input("Insira a coordenada 'x' do ponto: "))
y = float(input("Insira a coordenada 'y' do ponto: "))

if (x > 0 and x < 10) and (y > 0 and y < 10):
    print("Dentro do quadrado.")
elif (x == 0 or x == 10) and (y >= 0 and y <= 10):
    print("Na fronteira.")
elif (y == 0 or y == 10) and (x >= 0 and x <= 10):
    print("Na fronteira.")
else:
    print("Fora do quadrado.")