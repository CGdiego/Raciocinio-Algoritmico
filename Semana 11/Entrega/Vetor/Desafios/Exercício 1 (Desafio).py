valores = [10, 5, 3, 5, 2, 3, 3, 9, 2, 9, 9]
subst = 0
i = 0

while i < len(valores):
    repetido = False # Não há nenhum valor repetido no início
    ii = 0 # Novo índice
    while ii < i:
        if valores[i] == valores[ii]:
            repetido = True
        ii += 1
    if repetido:
        valores[i] = -999 # Seta o valor repitido pra -999
    i += 1

i = 0

while i < len(valores):
    if valores[i] != -999:
        valores[subst] = valores[i]
        subst += 1
    i += 1

while subst < len(valores):
    valores[subst] = -999
    subst += 1

print(valores)