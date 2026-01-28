numbers = list(range(1, 9))
reNumbers = numbers[::-1] # 리스트 뒤집기

inputNum = list(map(int, input().split()))

if numbers == inputNum:
    print("ascending")
elif reNumbers == inputNum:
    print("descending")
else:
    print("mixed")