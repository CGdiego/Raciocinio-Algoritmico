lista = []

for i in range(5):
    valor = input(f"Insira o {i+1}º valor inteiro positivo: ")
    
    while not valor.isdigit():
        valor = input(f"Insira o {i+1}º valor inteiro positivo: ")

    lista.append(int(valor))

lista2 = sorted(lista)

lista3 = sorted(lista, reverse=True)

print(f"{lista}\n{lista2}\n{lista3}")
print()
print(len(lista))
print()
print(min(lista))
print()
print(max(lista))
print()
print(sum(lista))