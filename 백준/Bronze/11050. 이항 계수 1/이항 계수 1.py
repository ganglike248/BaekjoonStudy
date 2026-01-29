def facto(n):
    NF = 1

    for i in range(1, n + 1):
        NF *= i

    return NF

N, K = map(int, input().split())

A = facto(N)
B = facto(K)
C = facto(N - K)

print(int(A / (B * C)))