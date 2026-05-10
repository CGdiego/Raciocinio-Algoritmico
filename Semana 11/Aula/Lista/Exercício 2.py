lista = []

for i in range(5):
    valor = input(f"Insira o {i+1}º valor inteiro positivo: ")
    
    while not valor.isdigit() and int(valor) < 0:
        valor = input(f"Insira o {i+1}º valor inteiro positivo: ")

    lista.append(valor)

lista2 = sorted(lista)

lista3 = sorted(lista, reverse=True)

print(f"{lista}\n{lista2}\n{lista3}")