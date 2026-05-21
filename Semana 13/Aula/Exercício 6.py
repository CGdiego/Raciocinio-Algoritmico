def imprime_diagonal(l0c0, l0c1, l0c2, l1c0, l1c1, l1c2, l2c0, l2c1, l2c2):
    matriz = [
        [l0c0, l0c1, l0c2],
        [l1c0, l1c1, l1c2],
        [l2c0, l2c1, l2c2]
    ]
    print(l0c0, l1c1, l2c2)

def main():
    imprime_diagonal(1, 2, 3, 4, 5, 6, 7, 8, 9)

main()