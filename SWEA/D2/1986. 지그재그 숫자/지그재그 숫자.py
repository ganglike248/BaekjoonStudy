for i in range(int(input())):
    sum = 0
    c = 1
    N = int(input())

    for j in range(1, N+1):
        sum += c * j
        c *= -1

    print(f'#{i+1} {sum}')