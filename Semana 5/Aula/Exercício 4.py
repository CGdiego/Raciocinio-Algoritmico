palavra = input("Digite uma palavra:\n")
tamanho = len(palavra)

while tamanho < 3 or tamanho > 10:
    print("A palavra deve ter no mínimo 3 letras e no máximo 10.")
    palavra = (input("Palavra válida:\n"))
    tamanho = len(palavra)

print("\n")
print(palavra)
print(tamanho)