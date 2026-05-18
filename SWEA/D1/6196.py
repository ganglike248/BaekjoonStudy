# 1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.


# 입력
# 9

# 출력
# 11106

a = int(input())
n = 0

for i in range(4):
    n += a * (10**i) * (4 - i)

print(n)