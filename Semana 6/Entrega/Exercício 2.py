conta = 0
n = 0

while n <= 0:
    n = int(input("Insira um número positivo: "))

if n > 0:
    for i in range(1,n+1):
        conta = conta + i
    print(f"O resultado da soma é {conta}.")