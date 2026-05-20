A = [0] * 6

A[0] = 1
A[1] = 0
A[2] = 5
A[3] = -2
A[4] = -5
A[5] = 7

soma = A[0] + A[1] + A[5]
print(soma)

A[4] = 100

for a in A:
    print(a)