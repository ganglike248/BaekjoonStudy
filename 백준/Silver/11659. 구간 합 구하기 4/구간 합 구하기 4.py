import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

sumList = [0]
t = 0

# 합 배열 만들기
for i in nums:
    t += i
    sumList.append(t)

# 입력 받기
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(sumList[e] - sumList[s-1])