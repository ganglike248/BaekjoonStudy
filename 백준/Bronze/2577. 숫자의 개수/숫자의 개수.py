A = int(input())
B = int(input())
C = int(input())

num = list(map(int, str(A*B*C)))

numbers = list(range(10))

for i in numbers:
    s = 0

    for j in num:
        if i == j:
            s += 1

    print(s)