caminho1 = input("Você está em uma floresta e precisa escolher um caminho para seguir. Você pode escolher: esquerda (E) ou direita (D). ").upper()

if caminho1 == "E":
    caminho2 = input("Você encontrou um rio. Você pode escolher: atravessar (A) ou voltar (V). ").upper()
    if caminho2 == "A":
        print("Você chega a uma vila segura.")
    elif caminho2 == "V":
        print("Você permanece perdido na floresta.")
elif caminho1 == "D":
    caminho3 = input("Você encontrou um rio. Você pode escolher: subir (S) ou voltar (V). ").upper()
    if caminho3 == "S":
        print("Você encontra um tesouro no topo.")
    elif caminho3 == "V":
        print("Você permanece perdido na floresta.")