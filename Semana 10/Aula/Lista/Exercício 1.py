import random

numerosJogador1 = []
numerosJogador2 = []

for i in range(3):
    num = random.randint(1, 6)
    numerosJogador1.append(num)

for i in range(3):
    num = random.randint(1, 6)
    numerosJogador2.append(num)

somaJ1 = sum(numerosJogador1)
somaJ2 = sum(numerosJogador2)

if somaJ1 > somaJ2:
    print("O jogador 1 venceu!")
elif somaJ2 > somaJ1:
    print("O jogador 2 venceu!")
else:
    print("O jogo empatou")