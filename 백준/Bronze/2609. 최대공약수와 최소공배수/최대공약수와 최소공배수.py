A, B = map(int, input().split())

maxNum = 0 # 최대공약수
minNum = 0 # 최소공배수

for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        maxNum = i

minNum = int(A * B / maxNum)

print(maxNum)
print(minNum)