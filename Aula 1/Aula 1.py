nome = input("Digite o seu nome: ")
cpf = input("Digite o seu CPF: ")
telefone = input("Digite o seu telefone: ")
ano = int(input("Digite o seu ano de nascimento: "))

# Método 1
print("Nome: " + nome)
print("CPF: " + cpf)
print("Telefone: " + telefone)
print("Ano: " + str(ano))

# Método 2
print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"Telefone: {telefone}")
print(f"Ano: {ano}")