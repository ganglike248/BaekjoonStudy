import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
count = 0
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def dfs(a):
    visited[a] = True
    for neighbor in arr[a]:
        if not visited[neighbor]:
            dfs(neighbor)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)