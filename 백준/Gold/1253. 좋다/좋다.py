import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort() # 정렬
count = 0 # 좋은 수 개수

for k in range(N):
    i = 0 # 왼쪽 끝
    j = N-1 # 오른쪽 끝

    find = A[k] # 비교할 수

    while i < j:
        # 두 수의 합이 find와 같으면
        if A[i] + A[j] == find:
            # 자기 자신이 포함 안되면
            if i != k and j != k:
                # 하나 추가
                count += 1
                break
            elif i == k:
                i += 1
            else:
                j -= 1
        # 찾을 수 보다 작으면
        elif A[i] + A[j] < find:
            # 왼쪽을 높여서 올려주기
            i += 1
        else:
            # 오른쪽을 낮춰서 내려주기
            j -= 1

print(count)