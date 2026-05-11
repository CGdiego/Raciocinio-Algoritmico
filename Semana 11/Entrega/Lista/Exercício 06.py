lista1 = []
lista2 = []

for i in range(1,11):
    if i % 2 == 0: # Verifica se é par
        lista1.append(i)
    else:
        lista2.append(i)

lista3 = lista1 + lista2 # Se não precisasse criar uma nova lista, poderia usar o .extend()

print(lista3)