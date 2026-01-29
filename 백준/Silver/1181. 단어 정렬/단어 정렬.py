N = int(input())
st = []


for i in range(N):
    S = input()

    if S not in st:
        st.append(S)

st = sorted(st, key=lambda x : (len(x), x))

for i in st:
    print(i)