conta = 0
n = 0

while n <= 0: # Enquanto n é menor ou igual a 0...
    n = int(input("Insira um número positivo: "))

for i in range(1,n+1):
    conta = conta + i # Conta é conta + i, sendo que i aumenta a cada loop
print(f"O resultado da soma é {conta}.")