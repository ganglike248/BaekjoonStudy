T = int(input())
F = 0 # 층
R = 0 # 호

for _ in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        F = H
        R = N // H
    else:
        F = N % H
        R = (N // H) + 1

    print(F * 100 + R)