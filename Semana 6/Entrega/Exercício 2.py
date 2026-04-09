n = int(input("Insira um número positivo: "))
conta = 0

if n > 0:
    for i in range(1,n+1):
        conta = conta + i
    print(f"O resultado é {conta}")