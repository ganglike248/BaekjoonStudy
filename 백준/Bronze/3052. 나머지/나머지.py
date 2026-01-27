nums = []
num = 0

for _ in range(10):
    num = int(input()) % 42
    if num not in nums:
        nums.append(num)

print(len(nums))