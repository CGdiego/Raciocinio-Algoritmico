nota = float(input("Insira sua nota:\n"))

print("\n")

while nota < 0 or nota > 10:
    nota = float(input("Insira uma nota válida:\n"))
    print("\n")
else:
    print("Tudo certo!")
