palavra = input("Digite uma palavra que comece com uma vogal: ")

# Pode ser escrito com "palavra.startswith[0]" também.

while palavra[0].lower() != 'a' and palavra[0].lower() != 'e' and palavra[0].lower() != 'i' and palavra[0].lower() != 'o' and palavra[0].lower() != 'u':
    print("Palavra inválida.")
    palavra = input("Insira uma nova palavra: ")

for letra in palavra:
    print(letra)