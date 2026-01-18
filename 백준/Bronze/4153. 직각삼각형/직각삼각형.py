while True:
    nums = list(map(int, input().split()))

    if all(x == 0 for x in nums):
        break

    nums = sorted(nums)

    if((nums[0]**2 + nums[1]**2) == nums[2]**2):
        print("right")
    else:
        print("wrong")