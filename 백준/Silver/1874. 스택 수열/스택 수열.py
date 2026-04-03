import sys

n = int(sys.stdin.readline())
stack = []
answer = []
c = 1

# 정수들 입력 받기
for _ in range(n):
    target = int(sys.stdin.readline())

    while c <= target:
        stack.append(c)
        answer.append("+")
        c += 1
    if stack[-1] == target:
        stack.pop()
        answer.append("-")
    else:
        # 스택 맨 위가 target이 아니라면
        print("NO")
        sys.exit()

for i in answer:
    print(i)