T = int(input())

for i in range(T):
    S = input()
    count = 0

    for j in S:
        if (j == "("):
            count += 1
        elif (j == ")"):
            count -= 1
        
        if count < 0:
            print("NO")
            break
    else:
        if count == 0:
            print("YES")
        else:
            print("NO")