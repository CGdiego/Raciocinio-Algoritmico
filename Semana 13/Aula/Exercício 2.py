def maior():
    n1 = int(input("Digite o 1º número: "))
    n2 = int(input("Digite o 2º número: "))
    n3 = int(input("Digite o 3º número: "))
    return max(n1, n2, n3)
    
def main():
    print(maior())

main()