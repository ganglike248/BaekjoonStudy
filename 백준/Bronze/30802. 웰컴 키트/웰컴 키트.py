import sys

# 참가자의 수
N = int(sys.stdin.readline())

# 티셔츠 사이즈별 신청자 수(리스트)
S = list(map(int, sys.stdin.readline().split()))

# 티셔츠 묶음 수 T, 펜 묶음 수 P
T, P = map(int, sys.stdin.readline().split())

# T장의 티셔츠 주문 묶음 수
TS = 0

# 티셔츠 묶음 수 구하기
for i in S:
    TS += int(i / T) + 1 # 몫에 +1 하기. 예를 들어 i가 3이고, T가 5라면, 몫은 0이라 카운트가 안 됨

    # 그래서 만약 i와 T가 같다면 몫은 1이어야 맞기 때문에 다시 -1을 빼준다
    if i % T == 0:
        TS -= 1

# 티셔츠를 T장씩 최소 몇 묶음 주문하는가
print(TS)

# 펜 묶음 수와 낱개 수
print(int(N / P), N % P)