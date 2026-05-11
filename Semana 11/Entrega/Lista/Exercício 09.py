import random

lista = []
posicaoF = 0

for i in range(26):
    lista.append(chr(97 + i)) # chr(97) é o 'a'

random.shuffle(lista) # Embaralha a lista

letra = random.randint(97, 122) # Escolha um caractere aleatório
letra = chr(letra)

for i in range(26):
    if lista[i] == letra:
        posicaoF = i + i

posicao = input(f"Digite a posição correta de '{letra}' (1-26): ")
while not posicao.isdigit() or int(posicao) > 26 or int(posicao) < 1:
    print("Inválido, insira novamente.\n")
    posicao = input(f"Digite a posição correta de '{letra}' (1-26): ")

print(f"\n{lista}")

if int(posicao) == posicaoF:
    print("Você acertou! :D")
else:
    print("Errou. :(")