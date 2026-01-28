T = int(input())

a = []

for _ in range(T):
    num = 0
    total = 0

    a = list(input())
    
    for i in a:
        if (i == "O"):
            num += 1
        else:
            num = 0

        total += num

    print(total)