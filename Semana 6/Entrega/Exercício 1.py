quant = 0

for i in range(101):  # De 0 até 100
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        quant += 1

print(f"{quant} números atingiram a condição.")