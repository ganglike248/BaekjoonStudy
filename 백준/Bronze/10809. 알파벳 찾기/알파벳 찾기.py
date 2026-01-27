import string

S = input()
nums = []
alpha = string.ascii_lowercase


for i in alpha:
    n = 0
    a = -1

    for j in S:
        if j == i:
            a = n
            break
        n += 1

    nums.append(a)

for i in nums:
    print(i, end=" ")