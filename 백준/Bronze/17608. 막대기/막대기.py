import sys

N = int(sys.stdin.readline())
stack = [] # 스택
top = 0 # 최근 가장 큰 값
count = 0 # 보이는 막대기 개수

# 입력 받기
for _ in range(N):
    num = int(sys.stdin.readline())
    stack.append(num)

# 가장 오른쪽 값부터
for k in reversed(stack):
    # 최근 가장 큰 값 보다 크면
    if top < k:
        # 가장 큰 값 업데이트
        top = k
        stack.pop()
        count += 1
    else:
        # 아니면 그냥 하나 제거
        stack.pop()

print(count)