import string

S = input()
nums = []
alpha = string.ascii_lowercase


for i in alpha:
    n = 0

    nums.append(S.find(i))

for i in nums:
    print(i, end=" ")