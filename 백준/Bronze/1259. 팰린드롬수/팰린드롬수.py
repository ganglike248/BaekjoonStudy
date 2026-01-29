while True:
    S = input()

    if S == "0":
        break

    RS = S[::-1]

    if S == RS:
        print("yes")
    else:
        print("no")