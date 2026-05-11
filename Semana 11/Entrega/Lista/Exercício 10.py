import time
print("\033[H\033[J", end="") # Limpa a tela do terminal

lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

while True:
    print(f"-=-==-===- Jogo da Velha -===-==-=-\n\n             {lista[0]} | {lista[1]} | {lista[2]}\n             —————————\n             {lista[3]} | {lista[4]} | {lista[5]}\n             —————————\n             {lista[6]} | {lista[7]} | {lista[8]}\n")

    X = input("Jogador X, escolha uma posição (1-9): ")
    while not X.isdigit() or int(X) > 9 or int(X) < 1 or lista[int(X) - 1] == "\033[1mX\033[0m" or lista[int(X) - 1] == "\033[1mO\033[0m":
        print("Posição inválida.\n")
        X = input("Jogador X, escolha uma posição (1-9): ")

    lista[int(X) - 1] = "\033[1mX\033[0m"

    if lista[0] == lista[1] == lista[2]:
        print("\033[H\033[J", end="")
        print("O jogador X venceu!")
        time.sleep(5)
        break
    elif lista[3] == lista[4] == lista[5]:
        print("\033[H\033[J", end="")
        print("O jogador X venceu!")
        time.sleep(5)
        break
    elif lista[6] == lista[7] == lista[8]:
        print("\033[H\033[J", end="")
        print("O jogador X venceu!")
        time.sleep(5)
        break
    elif lista[0] == lista[3] == lista[6]:
        print("\033[H\033[J", end="")
        print("O jogador X venceu!")
        time.sleep(5)
        break
    elif lista[1] == lista[4] == lista[7]:
        print("\033[H\033[J", end="")
        print("O jogador X venceu!")
        time.sleep(5)
        break
    elif lista[2] == lista[5] == lista[8]:
        print("\033[H\033[J", end="")
        print("O jogador X venceu!")
        time.sleep(5)
        break
    elif lista[0] == lista[4] == lista[8]:
        print("\033[H\033[J", end="")
        print("O jogador X venceu!")
        time.sleep(5)
        break
    elif lista[2] == lista[4] == lista[6]:
        print("\033[H\033[J", end="")
        print("O jogador X venceu!")
        time.sleep(5)
        break

    print("\033[H\033[J", end="") # Limpa a tela do terminal

    print(f"-=-==-===- Jogo da Velha -===-==-=-\n\n             {lista[0]} | {lista[1]} | {lista[2]}\n             —————————\n             {lista[3]} | {lista[4]} | {lista[5]}\n             —————————\n             {lista[6]} | {lista[7]} | {lista[8]}\n")

    O = input("Jogador O, escolha uma posição (1-9): ")
    while not O.isdigit() or int(O) > 9 or int(O) < 1 or lista[int(O) - 1] == "\033[1mX\033[0m" or lista[int(O) - 1] == "\033[1mO\033[0m":
        print("Posição inválida.\n")
        O = input("Jogador O, escolha uma posição (1-9): ")

    lista[int(O) - 1] = "\033[1mO\033[0m"

    if lista[0] == lista[1] == lista[2]:
        print("\033[H\033[J", end="")
        print("O jogador O venceu!")
        time.sleep(5)
        break
    elif lista[3] == lista[4] == lista[5]:
        print("\033[H\033[J", end="")
        print("O jogador O venceu!")
        time.sleep(5)
        break
    elif lista[6] == lista[7] == lista[8]:
        print("\033[H\033[J", end="")
        print("O jogador O venceu!")
        time.sleep(5)
        break
    elif lista[0] == lista[3] == lista[6]:
        print("\033[H\033[J", end="")
        print("O jogador O venceu!")
        time.sleep(5)
        break
    elif lista[1] == lista[4] == lista[7]:
        print("\033[H\033[J", end="")
        print("O jogador O venceu!")
        time.sleep(5)
        break
    elif lista[2] == lista[5] == lista[8]:
        print("\033[H\033[J", end="")
        print("O jogador O venceu!")
        time.sleep(5)
        break
    elif lista[0] == lista[4] == lista[8]:
        print("\033[H\033[J", end="")
        print("O jogador O venceu!")
        time.sleep(5)
        break
    elif lista[2] == lista[4] == lista[6]:
        print("\033[H\033[J", end="")
        print("O jogador O venceu!")
        time.sleep(5)
        break

    print("\033[H\033[J", end="") # Limpa a tela do terminal