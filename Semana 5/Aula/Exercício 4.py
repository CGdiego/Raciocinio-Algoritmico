palavra = input("Digite uma palavra:\n")
tamanho = len(palavra)

while tamanho < 3 or tamanho > 10:
    print("A palavra deve ter no mínimo 3 letras e no máximo 10.")
    numero = (input("Palavra válida:\n"))

print(palavra)
print(tamanho)