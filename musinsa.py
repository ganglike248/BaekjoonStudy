# N은 내가 원하는 숫자
# K는 받을 숫자의 개수
N, K = map(int, input().split())
num = []

for i in range(1, N + 1):
    num.append(i)

# 얘들은 1이상 N이하의 수 중 K개의 수
kNums = list(map(int, input().split())) # kNums = [1, 4]

# 출력: N보다 작은 수 중 kNums를 제외한 나머지 수들의 합
print(sum(num) - sum(kNums))

# 5에서 2개(1, 4)를 선정하면 2, 3, 5가 남고 얘들을 더하면 10이됨