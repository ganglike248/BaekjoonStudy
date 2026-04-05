from collections import Counter
import sys
input = sys.stdin.readline

words = list(input().strip().upper())

num = list(Counter(words).items())

num.sort(key=lambda x : -x[1])

if len(num) == 1:
    print(num[0][0])
elif num[0][1] == num[1][1]:
    print("?")
else:
    print(num[0][0])