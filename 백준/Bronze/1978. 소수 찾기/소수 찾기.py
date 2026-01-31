import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

count = 0

# 소수 찾기
for i in num:

    # 1은 소수가 아님
    if i == 1:
        continue

    for j in range(2, i):

        if i % j == 0:
            break
    else:
        count += 1

print(count)