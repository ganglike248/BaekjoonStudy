for testCase in range(int(input())):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print(f'#{testCase} 1')
    else:
        print(f'#{testCase} 0')