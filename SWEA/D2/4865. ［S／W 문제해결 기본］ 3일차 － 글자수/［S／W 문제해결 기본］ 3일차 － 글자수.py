for i in range(int(input())):
    str1 = input()
    str2 = input()
    d = {}

    for j in str1:
        d[j] = 0
    
    for k in str2:
        if k in str1:
            d[k] += 1
    
    print(f'#{i+1} {max(d.values())}')