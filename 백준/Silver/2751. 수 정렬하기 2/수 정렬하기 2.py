import sys

N = int(sys.stdin.readline())
st = []

for i in range(N):
    st.append(int(sys.stdin.readline()))

st = sorted(st)

for i in st:
    print(i)