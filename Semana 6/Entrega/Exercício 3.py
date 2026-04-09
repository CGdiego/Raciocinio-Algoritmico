n1 = int(input("Insira um número inicial: "))
n2 = int(input("Insira um número final: "))

for i in range(n1,n2+1):
    print(f"Tabuada do {i}:")
    for tabuada in range(1, 11):
        print(i * tabuada)
    print("\n")