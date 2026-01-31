import sys

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

answer = 0

# 세 수를 더해서 M과 가장 가까운 값 찾기
# 브루트 포스 알고리즘 사용
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            s = cards[i] + cards[j] + cards[k]

            # M과 같다면 정답을 찾은 것이니 종료
            if s == M:
                print(s)
                exit(0)
            # M보다는 작지만 가장 가까운 최선의 값을 찾았을 경우 기존 값 대체
            elif answer < s <= M:
                answer = s

print(answer)