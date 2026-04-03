import sys
input = sys.stdin.readline
# 재귀 깊이 제한 풀기
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
# 빈 2차원 배열 선언
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    # 무방향이라 양쪽으로 넣어주기
    arr[u].append(v)
    arr[v].append(u)

# 방문 유무
visited = [False] * (N + 1)
count = 0

# dfs 선언
def dfs(v):
    # 현재 노드 방문 처리
    visited[v] = True
    
    # 연결된 친구들 확인
    for neighbor in arr[v]:
        # 아직 방문 안 했다면
        if not visited[neighbor]:
            # 파고 들기
            dfs(neighbor)

for i in range(1, N + 1):
    # 방문 안 했다면
    if not visited[i]:
        # dfs로 연결된 곳 모두 True로 바꿔주고
        dfs(i)
        # 다 하면 한 사이클 추가
        count += 1

print(count)