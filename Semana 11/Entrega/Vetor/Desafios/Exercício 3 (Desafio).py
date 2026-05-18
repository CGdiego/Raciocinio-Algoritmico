valores = [4, -1, 0, -3, 5, -2, 7, -8]
i = 0

while i < len(valores): # Percorre o vetor inteiro
    if valores[i] < 0: # Caso seja negativo
        j = i
        while j > 0 and valores[j-1] >= 0: # Condições para não passar do índice 0 da lista e não substituir outros negativos
            # Troca dos valores
            temp = valores[j]
            valores[j] = valores[j-1]
            valores[j-1] = temp
            j -= 1
    i += 1

print(valores)