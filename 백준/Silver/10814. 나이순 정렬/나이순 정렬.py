import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
l = []

for _ in range(N):
    info = input().split(" ")
    l.append(info)

l.sort(key=lambda x : int(x[0]))

for i in l:
    print(f'{i[0]} {i[1]}')