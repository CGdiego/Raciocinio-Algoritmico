valores = [1, 2, 3, 4, 5, 6, 7]
tamanho = len(valores)
k = 3
i = 0

while i < k:
    temp = valores[tamanho-1] # Salva o último numa variável temporária
    j = tamanho-1
    while j > 0: # Move todo mundo pra direita
        valores[j] = valores[j-1]
        j -= 1
    valores[0] = temp # Coloca o valor da variável temporária no início
    i += 1 # Avança para o próximo

print(valores)